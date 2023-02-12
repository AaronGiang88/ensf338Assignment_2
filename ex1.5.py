from cProfile import label
from matplotlib import pyplot as py
import timeit

def fib2(n,store = {}):
    if n == 0 or n == 1:
        return n
    elif n in store:
        return store[n]
    else:
        num = fib2(n-1,store) + fib2(n-2,store)
        store[n] = num
        return num
    
def fib1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

xAxis = [i for i in range(35)]

fib1List = []
fib1Times = []
for x in range(35):
    startTime = timeit.default_timer()
    fib1List.append(fib1(x))
    fib1Times.append( (timeit.default_timer() - startTime ))


fib2List = []
fib2Times = []
for x in range(35):
    startTime = timeit.default_timer()
    fib2List.append(fib2(x))
    fib2Times.append( (timeit.default_timer() - startTime ))


py.plot(xAxis,fib1Times,label = "Fib 1 ")
py.plot(xAxis,fib2Times,label = "Fib 2 ")
py.legend()
py.show()