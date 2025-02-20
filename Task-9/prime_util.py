def is_prime(n):
    if n <= 1:
        print("Is Not a prime Number")
    for i in range(2,n):
        if n % i == 0:
            print("is not a Prime Number")
            return
    print("is a prime Number")