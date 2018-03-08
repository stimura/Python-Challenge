import csv
import os
import numpy as np

# initial titles
print("\nElection Results")
print("------------------------------")

voter_id = []
county = []
candidate = []

os.chdir("/Users/SamTimura/Desktop/GWU_HW/Assignment_3")
csvpath = os.path.join("PyPoll", "election_data_2.csv")

# Add the neccessary information to the empty lists
with open(csvpath, encoding="latin-1") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Total Votes
total_votes = len(voter_id)
print("Total Votes: " + str(total_votes))
print("------------------------------")

# List of candidates
candidate_list = np.unique(candidate)

candidate1 = []
candidate2 = []
candidate3 = []
candidate4 = []

for i in candidate:
    if i == candidate_list[0]:
        candidate1.append(i)
    elif i == candidate_list[1]:
        candidate2.append(i)
    elif i == candidate_list[2]:
        candidate3.append(i)
    elif i == candidate_list[3]:
        candidate4.append(i)

# calculate percentage of votes
candidate1_percentage = round(len(candidate1) / total_votes, 2) * 100
candidate2_percentage = round(len(candidate2) / total_votes, 2) * 100
candidate3_percentage = round(len(candidate3) / total_votes, 2) * 100
candidate4_percentage = round(len(candidate4) / total_votes, 2) * 100

# print candidates
print(candidate1[0] + ": " + str(candidate1_percentage) + "% (" + str(len(candidate1)) + ")")
print(candidate2[0] + ": " + str(candidate2_percentage) + "% (" + str(len(candidate2)) + ")")
print(candidate3[0] + ": " + str(candidate3_percentage) + "% (" + str(len(candidate3)) + ")")
print(candidate4[0] + ": " + str(candidate4_percentage) + "% (" + str(len(candidate4)) + ")")

# printing breaks
print("------------------------------")

candidate1_votes = len(candidate1)
candidate2_votes = len(candidate2)
candidate3_votes = len(candidate3)
candidate4_votes = len(candidate4)

winner = [candidate1_votes, candidate2_votes, candidate3_votes, candidate4_votes]

if max(winner) == candidate1_votes:
    print("Winner: " + str(candidate1[0]))
elif max(winner) == candidate2_votes:
    print("Winner: " + str(candidate2[0]))
elif max(winner) == candidate3_votes:
    print("Winner: " + str(candidate3[0]))
elif max(winner) == candidate4_votes:
    print("Winner: " + str(candidate4[0]))

# printing breaks
print("------------------------------")

print("\n")

# formatting for csv
formatted_candidate1_percentage = str(candidate1_percentage) + "%"
formatted_candidate2_percentage = str(candidate2_percentage) + "%"
formatted_candidate3_percentage = str(candidate3_percentage) + "%"
formatted_candidate4_percentage = str(candidate4_percentage) + "%"

# formatting for csv
if max(winner) == candidate1_votes:
    winning_candidate = candidate1[0]
elif max(winner) == candidate2_votes:
    winning_candidate = candidate2[0]
elif max(winner) == candidate3_votes:
    winning_candidate = candidate3[0]
elif max(winner) == candidate4_votes:
    winning_candidate = candidate4[0]

# Creating first row for csv
title_row = ["Total Votes", candidate1[0], candidate2[0], candidate3[0], candidate4[0], "Winner"]

# Creating a list for the results csv
results_list = [total_votes, formatted_candidate1_percentage, formatted_candidate2_percentage, formatted_candidate3_percentage, formatted_candidate4_percentage, winning_candidate]

# Writing onto file
output_file = "pypoll2_results.csv"

# creating and editing the new file with results
with open(output_file, "w", encoding="latin-1") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(title_row)
    writer.writerow(results_list)
