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
election_csv = os.path.join('Resources','election_data.csv')

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        Overall.append(row[1])
        elec_votes = len(Overall)

    #Add to count if value is loacated in column[2]
