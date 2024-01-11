''' nth fibonacci number
def fibonacci(n):
    if(n<=1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n),end=" ") '''

#dp
fibarray=[0,1]
def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n<len(fibarray):
        return fibarray[n]
    else:
        fibarray.append(fibonacci(n-1)+fibonacci(n-2))
        return fibarray[n]
print(fibonacci(12))


    

