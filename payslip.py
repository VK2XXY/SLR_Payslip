from datetime import datetime, date, time, timedelta

# Getting current date
today = date.today()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print ("Today's date is ", today)
print ("\n", "Year:", today.year,
       "\n", "Month:", today.month, 
       "\n","Day:", today.day, 
       "\n","Weekday:", today.weekday(),
       "\n","Weekday (name):", days[today.weekday()],
       "\n",)


# Getting current time
time = datetime.now()
print("It's", time, "now.")
print ("\n", "Time:", datetime.time(time),
       "\n", "Hour:", time.hour, 
       "\n","Minute:", time.minute, 
       "\n","Second:", time.second,
       "\n","Microsecond:", time.microsecond,
       "\n",)





#d = datetime.today() - timedelta(hours=22, minutes=50)

#d.strftime('%H:%M %p')

#print(d)


#s1 = '06:22:00'
#s2 = '24:13:00' # for example
#format = '%H:%M:%S'
#time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
#print(time)

monSTART = input("Enter something:")

print(type(monSTART))

