import sys
from datetime import datetime
from datetime import timedelta

# Question 1
dt = datetime.now()
time_string = dt.strftime("%X")
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        _date, _time, store, item, cost, payment = data
        print("{}\t{}\t{}\t{}\t{}\t{}".format(dt, time_string, store, item, cost, payment))


# Question 2
newTime = dt - timedelta(seconds=60) + timedelta(days=730)
print(newTime)


# Question 3
nextTime = timedelta(days=100, minutes=13, hours=10)
print(nextTime)


# Question 4
def function(feet, inches):
    time = datetime.now()
    tes = str(time) + ", feet: " + feet + ", inches: " + inches
    print(tes)


function("34", "45")

