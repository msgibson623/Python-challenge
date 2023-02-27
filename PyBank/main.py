#This is is the financial analysis for PyBank
import os
import csv

#Define Names
total_months = 0
net = 0
Date = []
changes = []
profit_loss = []

#Source is from budget_Data.csv
budget_csv = os.path.join('Python-challenge_2','Resources','budget_data.csv')

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:

    #Total number of months included in dataset
        total_months+=1
        

    #Net Total amount of Profit/Losses
        net+=int(row[1])
        

    #Append Date Column to new list
        Date.append(row[1])

    #Append Row Column to new list
        profit_loss.append(int(row[1]))

    #Calculate the profit/loss difference
        changes.append(profit_loss[total_months-1]-profit_loss[total_months-2])
        #print(profit_loss)
    
    #Sum of difference
        difference = sum(changes)

    #Calculate the average and divide by the total rows 
    # #round two decimal places
    try:
        average = round(difference/(len(changes)-1), 2) 
    except ZeroDivisionError:
            average = 0
            
    
        
    #Greatest increase in profit(Date & Amount)
    profit_increase = max(changes)
    increase = changes.index(profit_increase)
  
    
    #Greatest decrease in profit(Date & Amount)
    profit_decrease = min(changes)
    decrease = changes.index(profit_decrease)

#Write to text file
output_path = "pybank_analysis.txt"

file =  open(output_path, 'w') 

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${net} \n")
file.write(f"Average Change: ${average}\n")
file.write(f"Greatest Increase in Profits: {Date[increase]} (${profit_increase}) \n")
file.write(f"Greatest Decrease in Profits: {Date[decrease]} (${profit_decrease}) \n")

file.close()