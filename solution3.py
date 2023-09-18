# Write a function that returns the nth elements in the Fibonacci Sequence.
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(7))
