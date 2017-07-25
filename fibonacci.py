import sys

def fib(n):
    if n is 0:
        return 1
    elif n is 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = raw_input('supply an n to be calculcated from the fibonacci sequence:' )
    n = int(n)
    print( str(fib(n)) )
