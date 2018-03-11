import csv
import os
import numpy as np

# Prompt user which file they would like to use
print("Which file would you like to use? Maybe election_data_1.csv?")
filename = input(" ")

# initial titles
print("\nElection Results")
print("------------------------------")

voter_id = []
county = []
candidate = []

os.chdir("/Users/SamTimura/Desktop/GWU_HW/Assignment_3_copy")
csvpath = os.path.join("PyPoll", filename)

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

# Writing onto file
output_file = "pypoll_results.txt"

# creating and editing the new file with results
with open(output_file, 'w') as file_object:
    file_object.write("\nElection Results")
    file_object.write("\n------------------------------")
    file_object.write("\nTotal Votes: " + str(total_votes))
    file_object.write("\n------------------------------")
    file_object.write("\n" + candidate1[0] + ": " + str(candidate1_percentage) + "% (" + str(len(candidate1)) + ")")
    file_object.write("\n" + candidate2[0] + ": " + str(candidate2_percentage) + "% (" + str(len(candidate2)) + ")")
    file_object.write("\n" + candidate3[0] + ": " + str(candidate3_percentage) + "% (" + str(len(candidate3)) + ")")
    file_object.write("\n" + candidate4[0] + ": " + str(candidate4_percentage) + "% (" + str(len(candidate4)) + ")")
    file_object.write("\n------------------------------")
    if max(winner) == candidate1_votes:
        file_object.write("\nWinner: " + str(candidate1[0]))
    elif max(winner) == candidate2_votes:
        file_object.write("\nWinner: " + str(candidate2[0]))
    elif max(winner) == candidate3_votes:
        file_object.write("\nWinner: " + str(candidate3[0]))
    elif max(winner) == candidate4_votes:
        file_object.write("\nWinner: " + str(candidate4[0]))
