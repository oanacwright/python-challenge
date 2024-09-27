import csv

# Path to collect the data from the Resource Folder
csvpath = "C:/Users/oanaw/python-challenge/PyBank/Resources/budget_data.csv"

# Open csv file and skip header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Define and assign values to variables and list that are goig to be used 
    month=[]
    profit_loss=[]
    change=[]
    totalprofit=0
    maxprofit=0
    maxprofitmonth =" "
    minprofit=0
    minprofitmonth =" "
    
    # Append the Month and Profit_Loss lists for every row in csv file. Also calculate total profit
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(float(row[1]))
        totalprofit += float(row[1])

    # Create my Profit/Losses change list from profit_loss list
    for i in range (1, len(profit_loss)):
        change.append(profit_loss[i]-profit_loss[i-1])
       
    # Calculate min and max of my change list to determine the maximum and minimum profits
    maxprofit=max(change)
    minprofit=min(change)
    
    # Looking for the index of max and min profit to find the month //remeber to add 1 to index 
    for i in range (1, len(change)):
        if maxprofit == change[i]:
            maxprofitmonth=month[i+1]
        if minprofit == change [i]:
            minprofitmonth=month [i+1]

    # Calculating the average change for profit/losses
    avgprofchange=sum(change)/len(change)

# Priting results to locat terminal and round all values to 2 decimals and add $ sign
print("Finiancial Analysis")
print("---------------------------------------")
print("Total Months: " + str(len(month)))
print("Total: $ "  + format(totalprofit,'.2f'))
print("Average Change: $ " + format(avgprofchange,'.2f'))
print("Greatest Increase in Profits: " + maxprofitmonth + " ($ " + format(maxprofit,'.2f')+")")
print("Greatest Decrease in Profits: " + minprofitmonth + " ($ " + format(minprofit,'.2f')+")")

# Printing results to file "PyBank_analysis.txt" and round all values to 2 decimals and add $ sign
output_file = "C:/Users/oanaw/python-challenge/PyBank/Analysis/PyBank_analysis.txt"

with open(output_file,"w+") as file:
    file.write ("Finiancial Analysis\n")
    file.write ("---------------------------------------\n")
    file.write("Total Months: " + str(len(month))+"\n")
    file.write("Total: $ "  + format(totalprofit,'.2f')+"\n")
    file.write("Average Change: $ " + format(avgprofchange,'.2f')+"\n")
    file.write("Greatest Increase in Profits: " + maxprofitmonth + " ($ " + format(maxprofit,'.2f')+")\n")
    file.write("Greatest Decrease in Profits: " + minprofitmonth + " ($ " + format(minprofit,'.2f')+")\n")