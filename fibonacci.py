n = int(input("Enter a number: "))
a, b = 1, 1
fib = []

for i in range(n):
    fib.append(a)
    a, b = b, a+b

print(fib)