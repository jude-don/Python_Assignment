from datetime import datetime  
import xlsxwriter
paid = 5  # signifies 5 dollars per hour
# algorithm to obtain start date and time
task_name = input("Please enter the name of the task you undergoing: \n")
answer = input("Do you want to use system time? Please choose Y/N. \n")
if answer == "Y":
    dt = datetime.now()
    first_year = dt.year
    first_month = dt.month
    first_day = dt.day
    first_hour = dt.hour
    first_minute = dt.minute
else:  
    first_year = int(input("Please enter year of the start date: \n"))
    first_month = int(input("Please enter month of the start date figures from 1-12: \n"))
    first_day = int(input("Please enter day of start date: \n")) 
    first_time = input("Please enter time of start date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
    mylist = first_time.split(',')
    first_hour = int(mylist[0])
    first_minute = int(mylist[1])

# algorithm to obtain end date and time
second_year = int(input("Please enter year of the end date: \n"))
second_month = int(input("Please enter month of the end date in figures from 1-12: \n"))
second_day = int(input("Please enter day of end date: \n"))
second_time = int(input("Please enter time of end date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n"))
mylist1 = second_time.split(',')
second_hour = int(mylist1[0])
second_minute = int(mylist1[1])


# Algorithm to find time difference and hours
first_date = datetime(first_year,first_month,first_day,first_hour,first_minute)
second_date = datetime(second_year,second_month,second_day,second_hour,second_minute)
difference_between_datetimes = second_date - first_date
hours_calculated = difference_between_datetimes.total_seconds()/3600
total_amount_received = hours_calculated * paid
currency = "$"
print('He spent %f %s on a task' % (hours_calculated,'hours'))
print("\n")
print('He will receive %s %f' % (currency,total_amount_received))

# Converting to an Excel file
workbook = xlsxwriter.Workbook('TaskHistory.xlsx') 
worksheet = workbook.add_worksheet() 
  
#Setting Headers
worksheet.write('A1', 'TaskName') 
worksheet.write('B1', 'StartDate') 
worksheet.write('C1', 'StartTime') 
worksheet.write('D1', 'EndDate') 
worksheet.write('E1', 'EndTime') 
worksheet.write('F1', 'HoursSpent') 
worksheet.write('G1', 'AmountReceived') 


#Pushing date
worksheet.write('A2', task_name)
g = str(first_year)+"-"+str(first_month)+"-"+str(first_day)
worksheet.write('B2',g )  
h = str(first_hour)+":"+str(first_minute)
worksheet.write('C2', h) 
g1 = str(second_year)+"-"+str(second_month)+"-"+str(second_day)
worksheet.write('D2',g1 )  
h1 = str(second_hour)+":"+str(second_minute)
worksheet.write('E2', h1) 
worksheet.write('F2', str(hours_calculated)) 
worksheet.write('G2', str(total_amount_received)) 
workbook.close()