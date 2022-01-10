from datetime import date
from datetime import datetime
import calendar
import csv
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
import pygal

# temp = pd.Timestamp('2020-11-25')
# print(temp.dayofweek, temp.day_name())
dictInterval = {}
dictInterval_weekend = {}
filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    wr = open("newActivity.csv","w")
    wr.write(str (header[0]) + "," + str (header[1]) + ","+ str (header[2]))
    wr.write("\n")

    n = 0 
    for row in reader :
        interval = int(row[2])
        if(row[0] == "NA"):
            row[0] = 0
            n += 1
        steps = row[0]
        temp = pd.Timestamp(row[1])
        if temp.dayofweek <5:
            row.append("weekday")
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
        else:
            row.append("weekend")
            dictInterval_weekend.setdefault(interval,[])
            dictInterval_weekend[interval].append(int(steps))
        
        # row.append()
        wr.write(str(row[0]))
        wr.write(str (row[0]) + "," + str (row[1]) + ","+ str (row[2]) + "," + str (row[3]))
        wr.write("\n")
    
    wr.close()

listAveragePerInterval = []
listAveragePerInterval_weekend = []

for i in dictInterval.keys():
    listAveragePerInterval.append(st.mean(dictInterval.get(i)))

for i in dictInterval_weekend.keys():
    listAveragePerInterval_weekend.append(st.mean(dictInterval_weekend.get(i)))

hist = pygal.Bar()
hist.title = "Average per interval Weekday"
hist.x_title = "The interval"
hist.y_title = "Average per interval"
hist.x_labels = dictInterval.keys()
hist.add("Average steps",listAveragePerInterval)
hist.render_to_file('stepsversion2.svg')

hist = pygal.Bar()
hist.title = "Average per interval Weekend"
hist.x_title = "The interval"
hist.y_title = "Average per interval"
hist.x_labels = dictInterval_weekend.keys()
hist.add("Average steps",listAveragePerInterval_weekend)
hist.render_to_file('stepsversion3.svg')
    
print("The total number of missing values is ",n)
print("New dataset created")