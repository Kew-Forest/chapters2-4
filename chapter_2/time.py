time = int(input("The time of day 0-24 "))
hours = int(input("number of hours to wait "))

newtime = (time + hours) % 24
if newtime < 12:
    print (str(newtime)+" am")
else:
    print(str(newtime-12) + " pm")
