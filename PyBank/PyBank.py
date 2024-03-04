#Import our dependencies
import os, csv

#Declare our variables
months = []
profit_change = []
total = []
total_length = -1
i=0

#Open our csv file and perform our operations
with open('PyBank/Resources/budget_data.csv', 'r') as thingy:

    csvreader = csv.reader(thingy,delimiter=',')
    #Pop off the header
    header = next(csvreader)

    #Reading through the remaining rows
    for row in csvreader:
        months.append(row[0])
        total.append(int(row[1]))
        total_length+=1
    
    #Calculate profit changes
    while i < total_length:
        value = total[i+1]-total[i]
        profit_change.append(value)
        i = i+1

#Total Months    
total_months = len(months)

#Total Money
total_money = sum(total)

#Average Change
average_change = sum(profit_change)/len(profit_change)

#Greatest Increase Value
greatest_increase = max(profit_change)

#Greatest Increase Month
throwaway_1 = profit_change.index(greatest_increase)
greatest_increase_month = months[throwaway_1]

#Greatest Decrease Value
greatest_decrease = min(profit_change)

#Greatest Decrease Month
throwaway_2 = profit_change.index(greatest_decrease)
greatest_decrease_month = months[throwaway_2]


#Print our Results
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_money))
print("Average Change: " + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + "$" + str(greatest_decrease))


#Write our outputs
with open('PyBank_Output', 'w') as thingy:
    thingy.write("Financial Analysis\n")
    thingy.write("----------------------------\n")
    thingy.write("Total Months: " + str(total_months) + "\n")
    thingy.write("Total: $" + str(total_money) + "\n")
    thingy.write("Average Change: " + str(average_change) + "\n")
    thingy.write("Greatest Increase in Profits: " + str(greatest_increase_month) + "$" + str(greatest_increase) + "\n")
    thingy.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + "$" + str(greatest_decrease) + "\n")