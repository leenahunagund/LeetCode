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

'''Dynamic Programming is mainly an optimization over plain recursion. 
Wherever we see a recursive solution that has repeated calls for same inputs,
we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems,
so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial.

For example, if we write simple recursive solution for Fibonacci Numbers,
we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.

'''
    

