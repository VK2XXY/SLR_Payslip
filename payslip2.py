import datetime as dt

times = ["26:13", "06:22"]
fmt = '%D:%H:%M'
start = dt.datetime.strptime(times[1], fmt )
end = dt.datetime.strptime(times[0], fmt)
diff = (end - start)

#diff.total_seconds()


#(diff.days, diff.seconds, diff.microseconds)


print(diff)
print(type(diff))
