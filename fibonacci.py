n = int(input("Enter a number: "))

if n <= 0:
    print([])
elif n == 1:
    print([1])
else:
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)