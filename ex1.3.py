
store = {}
def func(n,store):
    print("calls")
    if n == 0 or n == 1:
        return n
    elif n in store:
        return store[n]
    else:
        num = func(n-1,store) + func(n-2,store)
        store[n] = num
        return num
    

print(func(5,store))

