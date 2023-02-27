#This is is the election results for PyPoll
import os
import csv

#Create dictionary to hold votes for each canidate
Votes = {}

#Name for total votes
Overall = []

#Name of canidates
Charles_Casper_Stockham = 0
Diana_DeGette = 0
Raymon_Anthony_Doane = 0

#Source is from budget_Data.csv
election_csv = os.path.join('Python-challenge_2','Resources','election_data.csv')

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        Overall.append(row[1])
        elec_votes = len(Overall)

    #Add to count if value is loacated in column[2]
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham += 1
        
        elif row[2] == "Diana DeGette":
            Diana_DeGette += 1

        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane += 1

    #Canidate Calculation
    canidate_1 = round((Charles_Casper_Stockham/elec_votes)*100,3)
    canidate_2 = round((Diana_DeGette/elec_votes)*100,3)
    canidate_3 = round((Raymon_Anthony_Doane/elec_votes)*100,3)

    # Dictionary to hold the number of votes
    Votes = {"Charles Casper Stockham": Charles_Casper_Stockham, "Diana DeGette": Diana_DeGette, "Raymon Anthony Doane": Raymon_Anthony_Doane }

    elec_winner = max(Votes, key=Votes.get)

#Write to text file
output_path = "election_result.txt"

file =  open(output_path, 'w') 


file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {elec_votes}\n")
file.write("----------------------------\n")
file.write(f"Charles Casper Stockham: {canidate_1}% ({Charles_Casper_Stockham})\n")
file.write(f"Diana DeGette: {canidate_2}% ({Diana_DeGette})\n")
file.write(f"Raymon Anthony Doane: {canidate_3}% ({Raymon_Anthony_Doane}) \n")
file.write("----------------------------\n")
file.write(f"Winner: {elec_winner}\n")

file.close()