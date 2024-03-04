#Import our dependencies
import os, csv

#Declare our variables
total_votes = 0 
candidates = []
candidate_votes = []
candidate_percentages = []
i=0

#Open our csv file and perform our operations
with open('PyPoll/Resources/election_data.csv', 'r') as thingy:
    
    file = csv.reader(thingy, delimiter=",")
    #Pop off the header
    csv_header = next(file)

    #Reading through the remaining rows
    for row in file:
        total_votes += 1
        test = row[2]

        #If the name is not in the candidates array it gets appended to the candidates array and a vote is added to the candidate_votes array
        if test not in candidates:
            candidates.append(test)
            candidate_votes.append(1)
        
        #If the name is in the candidates array the vote gets added to it's rightful index in the array
        else:
            candidate_votes[candidates.index(test)] += 1
    
    #Calculate percentages and add them to the array
    while i<len(candidate_votes):
        number = (candidate_votes[i]/total_votes)*100
        candidate_percentages.append(round(number, 3))
        i+=1
        
#Print our results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(str(candidates[0]) + ": " + str(candidate_percentages[0]) + "% (" + str(candidate_votes[0])+ ")")
print(str(candidates[1]) + ": " + str(candidate_percentages[1]) + "% (" + str(candidate_votes[1]) + ")")
print(str(candidates[2]) + ": " + str(candidate_percentages[2]) + "% (" + str(candidate_votes[2]) + ")")
print("-------------------------")
print(f"Winner: " + str(candidates[1]))
print("-------------------------")

#Write our outputs
with open('PyPoll_output', "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------\n")
    file.write(str(candidates[0]) + ": " + str(candidate_percentages[0]) + "% " + str(candidate_votes[0]) + "\n")
    file.write(str(candidates[1]) + ": " + str(candidate_percentages[1]) + "% " + str(candidate_votes[1]) + "\n")
    file.write(str(candidates[2]) + ": " + str(candidate_percentages[2]) + "% " + str(candidate_votes[2]) + "\n")
    file.write("-------------------------\n")
    file.write("Winner: " + str(candidates[1]) + "\n")
    file.write("-------------------------\n")