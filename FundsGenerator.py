from datetime import datetime  

paid = 5  # signifies 5 dollars per hour

# algorithm to obtain start date and time
task_name = input("Please enter the name of the task you undergoing: \n")
answer = input("Do you want to use system time? Please choose Y/N. \n")
if answer == Y:
    dt = datetime.now()
    first_year = dt.year
    first_month = dt.month
    first_day = dt.day
    first_hour = dt.hour
    first_minute = dt.minute
else:  
    first_year = input("Please enter year of the start date: \n")
    first_year = int(first_year)
    first_month = input("Please enter month of the start date figures from 1-12: \n")
    first_month = int(first_month)
    first_day = input("Please enter day of start date: \n")
    first_day = int(first_day)
    first_time = input("Please enter time of start date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
    mylist = first_time.split(',')
    first_hour = int(mylist[0])
    first_minute = int(mylist[1])

# algorithm to obtain end date and time
second_year = input("Please enter year of the end date: \n")
second_year = int(second_year)
second_month = input("Please enter month of the end date figures from 1-12: \n")
second_month = int(second_month)
second_day = input("Please enter day of end date: \n")
second_day = int(second_day)
second_time = input("Please enter time of end date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
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