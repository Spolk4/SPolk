import os
import csv

#Where is my file
Budget_data_csv = os.path.join("Budget_data.csv")
Output_path = os.path.join("Output.txt")
#set variables
month_change = []
month_count = 0
tot_profit_loss = 0

change = 0
change_list = []
previous_net = 0

average_change = 0

#Open my file
with open(Budget_data_csv, 'r') as csvfile:
    #Treat as csv file and read it
    csvreader=csv.reader(csvfile)
 # skip header next line of list
    header = next(csvreader)
	
 # loop through row via reader  
    for row in csvreader:
        profit_loss = int(row[1])
        month_count += 1
        tot_profit_loss += profit_loss
 #track the change in the list
        change = profit_loss - previous_net
        change_list.append(change)
        month_change.append(row[0])
        # preparing next iteration
        previous_net = int(row[1])

 #capture the max and mins
    greatest_increase = max(change_list)
    list_place=change_list.index(greatest_increase)
    greatest_month=month_change[list_place]

    greatest_decrease = min(change_list)
    list_place = change_list.index(greatest_decrease)
    least_month = month_change[list_place]

    #average the change 
    average_change = tot_profit_loss/month_count 

    # print with format       
    print(f"Total Month:  {month_count}")
    print(f"Total: $ {tot_profit_loss}")
    print(f"Average Change: $ {average_change}" )
    print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {least_month} (${greatest_decrease})")
    
    output_string = (f"Total Month:  {month_count}\n"
      f"Total: $ {tot_profit_loss}\n"
      f"Average Change: $ {average_change}\n"
      f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n"
      f"Greatest Decrease in Profits: {least_month} (${greatest_decrease})\n"
   )
    # write budget_data_csv back to text file
    #file =open(Budget_data_csv, 'w+')
    with open(Output_path, 'w')as filename:
       filename.write(output_string)