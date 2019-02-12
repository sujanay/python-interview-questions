import time
import matplotlib.pyplot as plt

n1 = list(range(10, 500, 10))
timeList = []

mysum = 0
for n in n1:
    start = time.time()
    mysum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mysum += sum([i, j, k])

    finish = time.time()

    timeList.append(round(finish-start, 2))

print("n:", n1)
print("time list", timeList)
plt.plot(n1, timeList)
plt.show()