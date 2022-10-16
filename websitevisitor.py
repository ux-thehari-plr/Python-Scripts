#Python program to create a website alarm

#Import the webbrowser and time module 
import webbrowser
import time 
  
# Taking website to be opened as input
link = input("Enter the link to website you want to open ->")

# Taking alarm time from the user
alarm = input("Set the website alarm time as (Format:- HH:MM:SS)(24 hour format) ->") 
  
# This is the actual time that we will use to print. 
Current_time = time.strftime("%H:%M:%S") 
  
# Printing current time untill alarm time
while (Current_time != alarm): 
    print ("Waiting, the current time is " + Current_time +" :-( " )
    Current_time = time.strftime("%H:%M:%S") 
    time.sleep(1) 

# Opening the webpage at alarm time
if (Current_time == alarm): 
    print ("WEBSITE IS OPENING :D") 
    webbrowser.open(link)