#!/usr/bin/env python3

from datetime import datetime, date, time, timedelta
import math

startDateStr = input ("Enter the week start date - DD/MM/YYYY :")

startDateArray = startDateStr.split("/")

startDate = datetime(int(startDateArray[2]), int(startDateArray[1]), int(startDateArray[0]))


#print(startDate)


print("\n You entered " + startDate.strftime("%A" ", " "%d" " of " "%B" " " "%Y") + "\n")



monStart = input("Enter Monday Start Time - HH:MM :")
monFinish = input("Enter Monday Finish Time - HH:MM :")
#tueStart = input("Enter Tuesday Start Time - HH:MM :")
#tueFinish = input("Enter Tuesday Finish Time - HH:MM :")



monStart = monStart.split(":")
monFinish = monFinish.split(":")

monDuration = ((int(monFinish[0]) * 60) + int(monFinish[1])) - ((int(monStart[0]) * 60) + int(monStart[1]))

print("\n\nShift Duration(HH:MM): " + str((math.floor(monDuration/60))) + ":" +  str( monDuration%60))
print("Shift Duration(HH.MM): ", round(monDuration/60, 2), "\n\n")
