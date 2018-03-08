#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

#Then convert and export the data to use the following format instead:

#Emp ID,First Name,Last Name,DOB,SSN,State
#214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#15,Samantha,Lara,09/08/1993,***-**-7526,CO
#411,Stacy,Charles,12/20/1957,***-**-8526,PA

import csv 
import os

emp_id = []
names = []
dob = []
ssn = []
state = []

os.chdir("/Users/SamTimura/Desktop/GWU_HW/Assignment_3")
csvpath = os.path.join("PyBoss", "employee_data1.csv")

# Add the neccessary information to the empty lists
with open(csvpath, encoding="latin-1") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        emp_id.append(row[0])
        names.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

first_name = []
last_name = []

# Split name to two lists
for name in names:
    first_name.append(name.split(" ")[0])
    last_name.append(name.split(" ")[0])

year = []
month = []
day = []

# Change format of date by splitting, then rearranging
for date in dob:
    year.append(date.split("-")[0])
    month.append(date.split("-")[1])
    day.append(date.split("-")[2])

new_dob = []

# Rearrange dates - mm/dd/yyyy
for i in range(len(year)):
    new_dob.append(month[i] + "/" + day[i] + "/" + year[i])

# Reformat SSN - ***-**-8166
ssn_1 = []
ssn_2 = []
ssn_3 = []

for x in ssn:
    ssn_1.append(x.split("-")[0])
    ssn_2.append(x.split("-")[1])
    ssn_3.append(x.split("-")[2])

print(ssn_3[2])
    
