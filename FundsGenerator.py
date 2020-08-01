from datetime import datetime
import time

#INTRO
username = input("Hi, I'm Elsie, your time and wage manager. What would you like me to call you?\n").title()
print("Nice to meet you %s!\n" % username)
print("I will help you know how long you worked and how much you earned for a task you're about to start or an already completed one.\n") 

PayRate = 5  # signifies 5 dollars per hour

# algorithm to obtain start date and time
task_name = input("Please enter the name of the task: \n")#specify name to easily identify task.
answer = input("Are you starting now?Please type Y for yes and N for no. I'll start the time if you choose Y \n")#ask if user is starting now
if answer == "Y" or answer == "y": # allow room for capitalization error
    print("All the best %s! Call out my name when you're done." %username)
   
    dt = datetime.now()
    first_year = dt.year
    first_month = dt.month
    first_day = dt.day
    first_hour = dt.hour
    first_minute = dt.minute

    while True:
        if input() == "Elsie" or "elsie":
            break
                  
    st = datetime.now()
    second_year = st.year
    second_month = st.month
    second_day = st.day
    second_hour = st.hour
    second_minute = st.minute
    

else:
    print("Oh! you already completed the task? Great! Hit the enter key and I'll tell you how long you worked and how much you earned.") 
    first_year = int(input("Please enter year of the start date: \n"))
 
    first_month = int(input("Please enter month of the start date figures from 1-12: \n"))
    if first_month == 2 and first_year%4 == 0:
        first_day = int(input("Please enter day of start date, remember this year february has 29 days: \n")) #if it's February in a leap year, we'd expect an input a number between 1 and 29
    elif first_month == 2 and first_year%4 != 0:
        first_day = int(input("Please enter day of start date, remember february has 28 days: \n"))#if it's February in a regular year, we'd expect an input a number between 1 and 28
    elif first_month in [9,4,6,11]:
        first_day = int(input("Please enter day of start date. should be between 1 and 30: \n"))# September, April, June and November have 30 days
    else:
        first_day = int(input("Please enter day of start date. should be between 1 and 31: \n"))    

    first_time = input("Please enter time of start date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
    mylist = first_time.split(',')
    first_hour = int(mylist[0])
    first_minute = int(mylist[1])

    # algorithm to obtain end date and time
    second_year = int(input("Please enter year of the end date: \n"))

    second_month = int(input("Please enter month of the end date figures from 1-12: \n"))

    second_day = int(input("Please enter day of end date: \n"))

    second_time = input("Please enter time of end date in 24 hour format, separated by commas. For example 12hours 30 minutes as 12,30: \n")
    mylist1 = second_time.split(',')
    second_hour = int(mylist1[0])
    second_minute = int(mylist1[1])


# Algorithm to find time difference and hours worked
first_date = datetime(first_year,first_month,first_day,first_hour,first_minute)

second_date = datetime(second_year,second_month,second_day,second_hour,second_minute)

difference_between_datetimes = second_date - first_date
hours_calculated = difference_between_datetimes.total_seconds()/3600
total_amount_received = hours_calculated * PayRate
currency = "$"
print('Great work %s! You spent %f minutes, which is %f %s on the task. And you earned %s%f' % (username,hours_calculated*60,hours_calculated,'hours',currency,total_amount_received))
print('Your bill is $200')
time.sleep(5)
print("Don't mind me, I'm just kidding.\nBye %s, hope to see you soon!" %username)

