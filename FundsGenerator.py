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
    first_year = int(input("Please enter year of the start date: \n"))
    #Let's validate the input for month? say should be between 1 and 12.
    first_month = int(input("Please enter month of the start date(should be between 1 and 12: \n"))
    
    #also, validation for day, so that 30 can't be entered for february(2)
    #if first_month == 2 and first_year%4 == 0:
    #   first_day = int(input("Please enter day of start date,remember! February has 29 days: \n"))
    #elif first_month == 2 and first_year%4 != 0:
    #   first_day = int(input("Please enter day of start date,remember! February has 28 days: \n"))
    
    first_day = int(input("Please enter day of start date: \n"))
    
    first_time = input("Please enter time of start date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
    mylist = first_time.split(',')
    first_hour = int(mylist[0])
    first_minute = int(mylist[1])

# algorithm to obtain end date and time
second_year = int(input("Please enter year of the end date: \n"))

second_month = int(input("Please enter month of the end date: \n"))

second_day = int(input("Please enter day of end date: \n"))

second_time = input("Please enter time of end date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
mylist1 = second_time.split(',')
second_hour = int(mylist1[0])
second_minute = int(mylist1[1])
