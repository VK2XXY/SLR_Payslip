from datetime import datetime, date, time, timedelta
import math

monStart = input("Enter Monday Start Time - HH:MM :")
monFinish = input("Enter Monday Finish Time - HH:MM :")
#tueStart = input("Enter Tuesday Start Time - HH:MM :")
#tueFinish = input("Enter Tuesday Finish Time - HH:MM :")


#print(tueStart)


monStartArray = monStart.split(":")
monFinishArray = monFinish.split(":")

monDuration = ((int(monFinishArray[0]) * 60) + int(monFinishArray[1])) - ((int(monStartArray[0]) * 60) + int(monStartArray[1]))
print(monDuration)

print(type(monDuration))

print((math.floor(monDuration/60)))
print(monDuration%60)
print((math.floor(monDuration/60)),":",monDuration%60)
print("Shift Duration(HH:MM): " + str((math.floor(monDuration/60))) + ":" +  str( monDuration%60))
