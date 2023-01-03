#Task: Analyze the financial records of your company
#Create a Python script that analyzes the records to calculate each of the following values:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

#Import Modules
import os
import csv

#CSV file path in PyBank
budget_data_csv = os.path.join("Resources","budget_data.csv")

#Declare Variables & Lists
count = 0
initial_profits = 0
total_profits = 0
total_change_profits = 0
date = [] 
profits = []
monthly_changes = []

#Open and read budget_data.csv 
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #Iterations
    for row in csvreader:    
        #Total Months count
        count += 1 
        date.append(row[0])
      
        #Calculate total profits
        profits.append(row[1])
        total_profits = total_profits + int(row[1])
        final_profits = int(row[1])
      
        #Calculate Average Changes
        monthly_change_profits = final_profits - initial_profits
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profits = final_profits
        average_change_profits = (total_change_profits/count)
      
        #Calculate Greatest Increase/Decrease
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
    
    #Print results to terminal
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profits))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

#Export Text File
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profits) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
