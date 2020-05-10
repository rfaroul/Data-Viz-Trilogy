# -*- coding: UTF-8 -*-

import csv
import os

budget_file = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("Resources", "pyBank_data.txt")

total_months = 0 #86
net_total = 0 #38382578
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999]
amounts = []
dates = []
total_change = 0
average_change = 0

with open(budget_file, newline="") as budgetfile:
    reader = csv.reader(budgetfile, delimiter=',')
    header = next(reader)
    #print(f"CSV Header: {header}")
    
    for row in reader:
        #list of the profit/loss amounts in the second column
        dates.append((row[0]))
        amounts.append(int(row[1]))
       
        #1. The total number of months included in the dataset
        total_months += 1 
        
        #2. The net total amount of "Profit/Losses" over the entire period 
        net_total += int(row[1]) #38382578

    print(f"total number of months in the dataset: {total_months}")
    print(f"net total of Profit/Losses over the entire period: ${net_total}")
        
        
        #3. The average of the changes in "Profit/Losses" over the entire period
    #net total changes / number of times there's been a change
        #LOGIC: (starting from the last row) 
    for i in amounts: #all changes (profits and losses)
        #list comprehension
        changes = [ amounts[i + 1] - amounts[i] for i in range(len(amounts) - 1) ]
  
    #4. The greatest increase in profits (date and amount) over the entire period      
        greatest_increase[1] = max(changes)
        date_of_increase = changes.index(max(changes))
        greatest_increase[0] = dates[date_of_increase]

    #5. The greatest decrease in losses (date and amount) over the entire period
        greatest_decrease[1] = min(changes)
        date_of_decrease = changes.index(min(changes))
        greatest_decrease[0] = dates[date_of_decrease]
        
        #get index of date of largest change
    for change in range(0, len(changes)):
        total_change = total_change + changes[change]
        average_change = round(total_change/len(changes), 2)
       
    print("greatest increase: ", str(greatest_increase))
    print("greatest decrease: ", str(greatest_decrease))                 
#    print(f"profits: {profits}")
    print(f"average of changes over entire period: ${average_change}")
    
output = (f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average  Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


with open(output_path, 'w', newline = '') as txt_file:
    txt_file.write(output)
    

    
    
    
    
    
    
    
    
    
    
    