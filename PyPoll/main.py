#Task: Help a small, rural town modernize its vote-counting process.
#Create a Python script that analyzes the votes and calculates each of the following values:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vot

#Import Modules
import os
import csv

#CSV file path in PyPoll
election_data_csv = os.path.join("Resources","election_data.csv")

#Declare Variables & Lists
count = 0
candidate_list = []
candidate_name = []
vote_count = []
vote_percent = []

#Open and read election_data_csv
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #Iterations
    for row in csvreader:
        #Toal Votes
        count += 1 
        candidate_list.append(row[2])
    
    #Candidates
    for x in set(candidate_list):
        candidate_name.append(x)
        y = candidate_list.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
    
    #Winner    
    winning_vote_count = max(vote_count)
    winner = candidate_name[vote_count.index(winning_vote_count)]
    
    #Print results to terminal
    print("-------------------------")
    print("Election Results")   
    print("-------------------------")
    print("Total Votes :" + str(count))    
    print("-------------------------")
    for i in range(len(candidate_name)):
        print(candidate_name[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    print("-------------------------")
    print("The winner is: " + winner)
    print("-------------------------")

#Export Text File
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate_name))):
        text.write(candidate_name[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")