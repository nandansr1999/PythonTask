def factorial(n):
    result = 1
    if n == 0 or n == 1:
        print("factorial: 1")
    for i in range(2, n+1):
        result *= i
        print(f"Factorial : {result}")

def fibonacci(s):
    