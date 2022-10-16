#Python program to open a website at specific time

#Import the webbrowser and time module 
import webbrowser
import time 
  
# Taking website to be opened as input
link = input("Enter the link to website you want to open ->")

# Taking specific time from the user
time_to_open = input("Set the website alarm time as (Format:- HH:MM:SS)(24 hour format) ->") 
  
# This is the actual time that we will use to print. 
Current_time = time.strftime("%H:%M:%S") 
  
# Printing current time untill specific time
while (Current_time != time_to_open): 
    print ("Waiting, the current time is " + Current_time +" :-( " )
    Current_time = time.strftime("%H:%M:%S") 
    time.sleep(1) 

# Opening the webpage at specific time
if (Current_time == time_to_open): 
    print ("WEBSITE IS OPENING :D") 
    webbrowser.open(link)