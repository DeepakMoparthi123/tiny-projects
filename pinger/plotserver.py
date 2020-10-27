import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []

with open('pingerdata.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
        z.append(float(row[2]))

plt.plot(x,y, label='speed')
plt.xlabel('time')
plt.legend()
plt.plot(x,z, label='ping')
plt.xlabel('time')
plt.legend()
plt.show()