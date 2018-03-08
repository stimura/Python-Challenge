import csv
import os
import statistics as stats

months = []
revenue = []
revenue_change = []

os.chdir("/Users/SamTimura/Desktop/GWU_HW/Assignment_3")
csvpath = os.path.join("PyBank", "budget_data_1.csv")

# Add the neccessary information to the empty lists
with open(csvpath, encoding="latin-1") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        months.append(row[0])
        revenue.append(row[1])
        
# Delete the 'Date' title from the dataset
del months[0]

# creating a sum function for total revenue
def sumList(number_list):
    theSum = 0
    for j in number_list:
        theSum = theSum + j
    return theSum

# Delete the 'Revenue' title from dataset
del revenue[0]

# Convert revenue into integers
revenue = list(map(int, revenue))

# Total Revenue
total_revenue = sumList(revenue)

# Calculate changes in revenue
length_rev = len(revenue)
for i in range(length_rev):
    change = revenue[i] - revenue[i - 1]
    revenue_change.append(change)

# Delete first number that doesn't belong
del revenue_change[0]

# Creating a variable for the length of the months list
length_mon = len(months)

# Creating a variable for average revenue change
avg_revenue_change = stats.mean(revenue_change)

# Print header, total months, total revenue, average revenue change
print("Financial Analysis:")
print("-------------------------------")
print("Total Months: " + str(length_mon))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(avg_revenue_change))

# Adding zero to the first value in revenue change for indexing purposes
revenue_change.insert(0, 0)

# defining variable
max_change = max(revenue_change)
min_change = min(revenue_change)

# Creating a dictionary for the greatest increase/decrease in revenue information
dictionary = dict(zip(revenue_change, months))

# Printing the greatest increase and decrease in revenue
print("Greatest Increase in Revenue: " + dictionary[max_change] + " ($" + str(max_change) + ")")
print("Greatest Decrease in Revenue: " + dictionary[min_change] + " ($" + str(min_change) + ")")

# Creating a variable for greatest increase and decrease
greatest_increase = str(dictionary[max_change]) +" : "+ str(max_change)
greatest_decrease = str(dictionary[min_change]) +" : "+ str(min_change)
 
# Creating a list for the results csv
results_list = [length_mon, total_revenue, avg_revenue_change, greatest_increase, greatest_decrease]

# Writing onto file
output_file = "pybank1_results.csv"

# creating and editing the new file with results
with open(output_file, "w", encoding="latin-1") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Total Months", "Total Revenue", "Average Revenue Change", "Greatest Increase in Revenue", "Greatest Decrease in Revenue"])
    writer.writerow(results_list)
