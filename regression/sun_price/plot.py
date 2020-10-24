import csv
import matplotlib.pyplot as plt
import numpy as np

x, y = [], []

with open('train.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        sun_hours, price = float(row[1]), float(row[2])
        x.append(sun_hours)
        y.append(price)

plt.plot(x, y, 'ro', markersize=1)
def f(t):
    return 0.0544 * t + 1434
t1 = np.arange(1200, 3500, 1)
plt.plot(t1, f(t1), 'b.', markersize=1)
plt.xlabel('Sunshine hours per year')
plt.ylabel('Price per square meter')
plt.axis([1200, 3500, 500, 6000])
plt.show()