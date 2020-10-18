import csv
import matplotlib.pyplot as plt
import numpy as np

x, y = [], []

with open('train.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        town_code, unemployment, price = row[0], row[1], row[2]
        x.append(float(unemployment))
        y.append(float(price))

plt.plot(x, y, 'ro', markersize=1)
def f(t):
    return -9.03 * t + 1525
t1 = np.arange(0, 20, 0.01)
plt.plot(t1, f(t1), 'b.', markersize=1)
plt.xlabel('Unemployment %')
plt.ylabel('Price per square meter')
plt.axis([0, 20, 1000, 15000])
plt.show()