"""
Write a Python program to solve the general version of the above problem.
Ask the user for the time now (in hours 0-24), and ask for the number of hours to wait.
Your program should output what the time will be on the clock when the alarm goes off.
"""
timenow = float(input("What time is it now 0-24 "))
hourswait = float(input("How many hours are you waiting? "))

alarmtime = hourswait % 24 + timenow
alarmtime = alarmtime % 24
if alarmtime > 12:
    alarmtime = alarmtime % 12
    print("your alarm will go off at: " + str(alarmtime) + " PM")
else:
    print("your alarm will go off at: " + str(alarmtime) + " AM")

#print("your alarm will go off at: " + str(alarmtime))