def fib(n):
    if n <= 2:
        return 1
    n1, n2 = 1, 1
    
    i = 3
    while i <= x:
        i += 1
        n1, n2 = n2, n1 + n2
    return n2

for x in range(1,11):
    print(fib(x))