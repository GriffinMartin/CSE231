# ==============================================================================
# Computer Project 9
# ------------------------------------------------------------------------------
# This program processes agricultural data, namely the adoption of different
# Genetically Modified (GM) crops in the U.S. It first asks the user for two
# data files, one for food crop and another for non-food crop. It then computes
# some statistics on the data, such as average percentage planting rates and
# max-adoption rates. All the data is stored in dictionaries 
# ==============================================================================

# ------------------------------------------------------------------------------
# SYMBOL CONSTANTS
# ------------------------------------------------------------------------------
CROP_FILENAME = 'food_crop.csv' # Food crop file name (for debugging purposes)
NON_CROP_FILENAME = 'non-food_crop.csv' # Non-food crop file name (same)

# ------------------------------------------------------------------------------
# FUNCTION  open_files()
#   Prompts the user for file names and try to open them. If successful,
# returns two file objects in a list. Otherwise, prints error and returns empty
# list to the user.
# ------------------------------------------------------------------------------
def open_files():
    print('=' * 60)
    crop_prompt = 'Input filename for food crop: '
    non_crop_prompt = 'Input filename for non-food crop: '
    crop_file = input(crop_prompt) # Prompt for two file names
    non_crop_file = input(non_crop_prompt)
    try: # Attempt to open them
        crop_fp = open(crop_file, 'r')
        non_crop_fp = open(non_crop_file, 'r')
        return (crop_fp, non_crop_fp)
    except:
        print('Error: One of the file couldn\'t be opened. Exiting.')
        print('=' * 60)
        return ()

# ------------------------------------------------------------------------------
# FUNCTION  process_line(line)
#   Gets an entry line and matches the state (1st element) as the key and the
# rest as data points. Transforms values to integers and replaces missing values
# with -1 for later computations. Returns (key, value) pair.
# ------------------------------------------------------------------------------
def process_line(line):
    entry = line.split(',') # Split line by commas
    key = entry[0] # First item is state
    val = [(int(x) if x else -1) for x in entry[1:]] # Rest is data points
    return (key, val)

# ------------------------------------------------------------------------------
# FUNCTION  read_files(crop_fp, non_crop_fp)
#   Extracts data from both file by building two dictionaries with states as
# keys and data numbers as values. Ignores lines beginning with '#' or
# 'Years' (header).
# ------------------------------------------------------------------------------
def read_files(fp, cropD, nonCropD):
    crop_fp, non_crop_fp = fp[0], fp[1] # Split file object points
    for line in crop_fp:
        if line.startswith('#') or line.startswith('Years'):
            continue # Skip headers
        (key, val) = process_line(line) # Find data
        cropD[key] = val # Store it
    for line in non_crop_fp:
        if line.startswith('#') or line.startswith('Years'):
            continue
        (key, val) = process_line(line)
        nonCropD[key] = val
    return (cropD, nonCropD)

# ------------------------------------------------------------------------------
# FUNCTION  get_avg_pct(key, crop_type)
#   Computes average percentages of a data entry. If crop_type is 1, then the
# average is computed on food crop data and stored in the corresponding
# dictionary. If crop_type is 0, we do the same thing for non-food crop.
# Returns average percentages.
# ------------------------------------------------------------------------------
def get_avg_pct(key, crop_type, cropD, nonCropD):
    if crop_type: # Select desired crop dictionary
        key_list = list(cropD.keys())
    else:
        key_list = list(nonCropD.keys())
    if key in key_list: # Get the right dictionary entry
        data = cropD[key] if crop_type else nonCropD[key]
        data = data[:-1] # Discard last entry (2015)
        data[:] = [x for x in data if x != -1] # Only do math on valid data
        return (sum(data) / float(len(data)))
    else:
        return -1

# ------------------------------------------------------------------------------
# FUNCTION  get_adopt_rate(key, crop_type, cropD, nonCropD, year)
#   Computes max-adoption rate of a data entry. If crop_type is 1, then the rate
# is computed on food crop data and stored in the corresponding dictionary.
# If crop_type is 0, we do the same thing for non-food crop.
# ------------------------------------------------------------------------------
def get_adopt_rate(key, crop_type, cropD, nonCropD, year):
    data = cropD[key] if crop_type else nonCropD[key]
    data = data[:-1] # Discard last entry again
    (min_val, min_index, max_val, max_index) = find_min_max_indices(data)
    min_yr = year + min_index # Add offset to get correct year
    max_yr = year + max_index
    rate = (min_val - max_val) / float(min_yr - max_yr) # Compute rate
    return (rate, min_yr, max_yr)

# ------------------------------------------------------------------------------
# FUNCTION  find_min_max_indices(data)
#   Finds the minimum and maximum values inside data. Since data may have
# missing values, we identify the minimum actual value in data (not -1).
# Returns indices for both max and min values to match with a year.
# ------------------------------------------------------------------------------
def find_min_max_indices(data):
    sorted_d = sorted(data) # Sort data
    max_val = sorted_d[-1] # Get maximum value
    max_index = data.index(max_val) # Get corresponding index in data
    min_index = 0
    for i in range(len(sorted_d)): # Find second largest index
        if sorted_d[i] == -1:
            min_index += 1
        else:
            break
    min_val = sorted_d[min_index] # Get corresponding value in sorted list
    min_index = data.index(min_val) # Get its index in data
    return (min_val, min_index, max_val, max_index)

# ------------------------------------------------------------------------------
# FUNCTION  compute_stats(cropD, nonCropD, avgD, cropRateD, nonCropRateD, year)
#   Calculates various statistics on the given data, and stores them into their
# respective dictionary. Returns the statistics dictionaries.
# ------------------------------------------------------------------------------
def compute_stats(cropD, nonCropD, avgD, cropRateD, nonCropRateD, year):
    # Union of all cropD and nonCropD keys
    states = list(set(list(cropD.keys()) + list(nonCropD.keys())))
    for key in states: # Compute average percentages
        crop_avg = get_avg_pct(key, 1, cropD, nonCropD)
        non_crop_avg = get_avg_pct(key, 0, cropD, nonCropD)
        avgD[key] = (crop_avg, non_crop_avg)
    for key in list(cropD.keys()): # Compute max-adoption rates for food crop
        cropRateD[key] = get_adopt_rate(key, 1, cropD, nonCropD, year)
    for key in list(nonCropD.keys()): # Compute max-adoption rates for non-food crop
        nonCropRateD[key] = get_adopt_rate(key, 0, cropD, nonCropD, year)
    return (avgD, cropRateD, nonCropRateD)

# ------------------------------------------------------------------------------
# FUNCTION  display_stats()
#   Nicely formats data in 3 columns and outputs it to the user.
# ------------------------------------------------------------------------------
def display_stats(avgD, cropRateD, nonCropRateD, crop_name, non_crop_name):
    template_avg = '{:<15}{:>25}{:>20}' # Column template for means
    template_rate = '{:<15}{:>15}{:>15}{:>15}' # Column template for rates

    print('=' * 60) # Print header
    print(template_avg.format('State', 'Food Crop', 'Non-Food Crop'))
    print('')
    # Print all entry in alphabetical order
    for key in sorted(avgD):
        val = avgD[key]
        crop_avg = format_entry(val[0], 1)
        non_crop_avg = format_entry(val[1], 1)
        row = (key, crop_avg, non_crop_avg)
        print(template_avg.format(*row))

    print('=' * 60) # Print header
    print('Percent Max-Adoption Rate for Food Crop\nCrop: ' + crop_name)
    print('-' * 60)
    print(template_rate.format('State', 'Rate', 'Min-Year', 'Max-Year'))
    print('')
    # Print all entry in descending order
    for key in reversed(sorted(cropRateD, key = cropRateD.get)):
        val = cropRateD[key]
        rate, min_yr, max_yr = format_entry(val[0], 0), val[1], val[2]
        row = (key, rate, min_yr, max_yr)
        print(template_rate.format(*row))

    print('=' * 60) # Print header
    print('Percent Max-adoption Rate for Non-Food Crop\nCrop: ' + non_crop_name)
    print('-' * 60)
    print(template_rate.format('State', 'Rate', 'Min-Year', 'Max-Year'))
    print('')
    # Print all entry in descending order
    for key in reversed(sorted(nonCropRateD, key = nonCropRateD.get)):
        val = nonCropRateD[key]
        rate, min_yr, max_yr = format_entry(val[0], 0), val[1], val[2]
        row = (key, rate, min_yr, max_yr)
        print(template_rate.format(*row))
    print('=' * 60)

# ------------------------------------------------------------------------------
# FUNCTION  format_entry(entry)
#   Converts -1 (missing values) to 'N/A' for average percentages. Forces floats
# to have 3 digits after the decimal point and adds a '+' in front of positive
# values for max-adoption rates.
# ------------------------------------------------------------------------------
def format_entry(entry, entry_type):
    if entry_type:
        if entry == -1:
            return 'N/A'
        else:
            return '{:.3f}'.format(float(entry))
    else:
        formatted_entry = '{:.3f}'.format(float(entry))
        if entry > 0:
            return '+' + formatted_entry
        else:
            return formatted_entry

# ------------------------------------------------------------------------------
# FUNCTION  extract_crop_data(fp)
#   Extracts data from crop files: beginning year, food crop name
# and non-food crop name. Returns them to user.
# ------------------------------------------------------------------------------
def extract_crop_data(fp):
    crop_fp, non_crop_fp = fp[0], fp[1] # Split file object pointers
    for line in crop_fp:
        if line.startswith('# crop name: '):
            crop_name = line.split()[-1] # Get food crop name
            continue
        if line.startswith('Year'):
            year = int(line.split(',')[1]) # Get beginning year
            break # and break since we're done
    for line in non_crop_fp:
        if line.startswith('# crop name: '):
            non_crop_name = line.split()[-1] # Get non-food crop name
            break
    return (year, crop_name, non_crop_name)

# ------------------------------------------------------------------------------
# MAIN PROGRAM STARTS HERE
#   We use 5 dictionaries. cropD and nonCropD stores the raw data provided in
# food_crop.csv and non-food_crop.csv by state avgD stores
# average planting rate for food and non-food crops. cropRateD and nonCropRateD
# stores max-adoption rate by state for food and non-food crops.
# ------------------------------------------------------------------------------
def main():
    cropD, nonCropD = {}, {} # Raw data dictionaries
    avgD, cropRateD, nonCropRateD = {}, {}, {} # Statistics dictionaries
    # Open both files
    fp = open_files()
    if fp == (): # If one file cannot be opened
        return # Exit
    # Get crop data
    (year, crop_name, non_crop_name) = extract_crop_data(fp)
    # Read raw data into dictionaries
    (cropD, nonCropD) = read_files(fp, cropD, nonCropD)
    # Compute statistics on raw data and store them into new dictionaries
    (avgD, cropRateD, nonCropRateD) = compute_stats(cropD, nonCropD, avgD, cropRateD, nonCropRateD, year)
    # Print stats to the user, nicely formatted
    display_stats(avgD, cropRateD, nonCropRateD, crop_name, non_crop_name)

# ------------------------------------------------------------------------------
main() # Launch program
