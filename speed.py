# test script to measure speed of system

import time
start = time.time()

list = []

# create a for loop that calculates pi 3 times
for i in range(0, 3):
    i = i + 1
    print(f"Adding {i} to the list.")
    list.append(i)

end = time.time()
print(end - start)
