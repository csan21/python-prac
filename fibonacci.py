# fibonacci recursion [0, 1, 1, 2, 3, 5, etc]
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
# print(fib(5)) output: 5
