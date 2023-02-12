import sys
import json
import timeit
from matplotlib import pyplot as py

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


with open("ex2.json", "r") as read_file:
    data = json.load(read_file)

sortedListTimes = []
lengthOfArray = []


for x in data:
    startTime = timeit.default_timer()
    func1(x,0,(len(x)-1))
    sortedListTimes.append((timeit.default_timer() - startTime))
    lengthOfArray.append(len(x))
    print(sortedListTimes)
    print(lengthOfArray)
    


py.plot(lengthOfArray,sortedListTimes)
py.show()