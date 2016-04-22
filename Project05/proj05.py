# -*- coding: utf-8 -*-

###########################################################
# Computer Project 5
# Job Salaries in the US - This program asks the user for
# a file name (from data.gov) and a keyword. It then:
#    Finds all jobs matching this keyword
#    Displays their corresponding salary
#    Displays minimum and maximum salary, and average
###########################################################


while(1):
    # Prompt user for a file
    fileName = input('\nEnter a file name: ')
    # Try opening the file
    try:
        fp = open(fileName, 'r')
    except:
        print('File not found, try again.')
        continue

    # Prompt user for a job keyword and convert to lowercase
    keyWord = input('Enter an occupational keyword: ').lower()
    # Initialize comparison values
    minSalary = 10e10
    job = minJob = maxJob = ""
    avgSalary = jobCount = maxSalary = 0

    # Print headers
    print('\nSalary\t\tOccupation\n')
    # Loop through each line to get job salaries
    for line in fp:
        if (keyWord in line.lower()):
            # Get salary and try to convert it to integer
            salary = line[172:182].strip()
            try:
                salary = int(salary)
            except:
                continue
            # Get occupation title and check for duplicates
            if (job == line[10:120].strip()):
                continue
            else:
                job = (line[10:120].strip())
            # Calculate avarage salary
            avgSalary = (avgSalary*jobCount + salary) / (jobCount + 1)
            jobCount += 1
            # Check for minimum and maximum values
            if (salary < minSalary):
                minSalary = salary
                minJob = job
            if (salary > maxSalary):
                maxSalary = salary
                maxJob = job
            # Print each matching job with their salary
            print('$ ' + '{:,}'.format(salary) + '\t' + job)

    # Print minimum and maximum jobs and the average of all jobs found
    #This uses the format() function 
    print('\nMin: ' + '$ ' + '{:,}'.format(minSalary) + '\t' + minJob)
    print('Max: ' + '$ ' + '{:,}'.format(maxSalary) + '\t' + maxJob + '\n')
    print('Accross ' + str(jobCount) + ' jobs the average salary was $ ' + '{:,}'.format(avgSalary))
    #ends program after solving average
    break 
