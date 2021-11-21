#initialize variables to store data used to compute the final output

#Variable to count the number of months included in the dataset
month_num = 0
#pl_total to store p&l from each iteration
pl_subtotal = 0
#pl_total to sum pl_subtotal from each iteration
pl_total = 0
#monthly_diff to store diff of t minus t-1 of p&l from each iteration
monthly_diff = int
#monthly_diff_total to store total of monthly_diff from each iteration
monthly_diff_total = 0
#variable to store current p&l change to transfer to t-1 at the end of the for loop
diff_spot = 0
#variable to store the greatest profit
g_profit = 0
#variable to store the greatest loss
g_loss = 0
#variable to compute average p&l change
avg_change = 0

#read csv file stored in the local folder
#not using path from pathlib
import csv
with open('budget_data.csv', 'r') as infile:
    #specifying "," as delimiter to split column information
    reader = csv.reader(infile, delimiter = ",")
    #initializing the csv to read from the first row, excluding the column lables
    header = next(reader)

    #record_max and min initialized as list to store date and amount for greatest loss and profit in loop
    record_max = []
    record_min = []
    #variable to store the current p&l as t-1 p&l for next iteration
    diff_lag = 0
    #for loop to iterate through each row in the data set
    for row in reader:
        #pl_subtotal, diff_spot holding the p&l value in the first interation
        pl_subtotal = int(row[1])
        #diff_spot for current p&l
        diff_spot = int(row[1])
        #pl_total to sum pl_subtotal from each iteration
        pl_total += pl_subtotal
        #monthly_diff is difference of t and t-1; diff_lag for t-1 = 0 for first iteration.
        monthly_diff = diff_spot - diff_lag
        #if condition to exclude the diff from first row for lack of a previos row
        if monthly_diff == diff_spot:
            monthly_diff = 0
        #monthly_diff_total summing up the difference from each month    
        monthly_diff_total += monthly_diff
        #assigning current p&l difference as t-1 for next iteration
        diff_lag = diff_spot
        #plus 1 to the count of data
        month_num += 1

        #if conditions to assign greatest increase and decrease im profits.   
        #activating the if condition regardless of current iteration of monthly diff value
        if g_loss == 0:
            #assigning the first iteration of monthly diff
            g_loss = monthly_diff
            #holding the data of the current iteration in a list i.e date and amount
            record_min = row
            #comparisons of other iterations with existing value
        elif monthly_diff < g_loss:
            g_loss = monthly_diff
            record_min = row
            #similar logic for max value as elif statement is true by default.
        elif monthly_diff > g_profit:
            g_profit = monthly_diff
            record_max = row

#calculate avg of monthly diff total, divided by n-1 count, adjusting for first row being zero.        
avg_change = round(monthly_diff_total / (month_num - 1), 2)
 
#print statements for output    
# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: ", month_num)
# print(f"Total: $",'{:,.2f}'.format(pl_total))
# print(f"Average Change: ", '${:,.2f}'.format(avg_change))
# print(f"Greatest Increase in Profits: ", record_max[0],"-", '${:,.2f}'.format(g_profit))
# print(f"Greatest Decrease in Profits: ", record_min[0],"-",'${:,.2f}'.format(g_loss))

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_num))
print("Total: $" + str('{:,.2f}'.format(pl_total)))
print("Average Change: " + str('${:,.2f}'.format(avg_change)))
# print(f"Greatest Increase in Profits: ", record_max[0],"-", '${:,.2f}'.format(g_profit))
# print(f"Greatest Decrease in Profits: ", record_min[0],"-",'${:,.2f}'.format(g_loss))

#Your final script should print the analysis to the terminal and export a text file with the results.

f = open("Financial Analysis Output.txt", "w")
f.write ("Financial Analysis")
f.write ("\n________________________________")
f.write ("\nTotal Months: " + str(month_num))
f.write ("\nTotal Profit & Loss: $" + str(pl_total))
f.write ("\nAverage P&L change: $" + str(avg_change))
f.write ("\nGreatest Increase in Profits: " + str(record_max[0])+ " $ " + str(g_profit))
f.write ("\nGreatest loss on record: " + str(record_min[0]) + " $ " + str(g_loss))
f.close()


      