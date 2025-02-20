def reverse_palindrome(s):
    r = s[::-1]
    print(f"The reverse of the given string is {r}")
    t = s.lower()
    u = t[::-1]
    if t == u :
        print("Is palindrome")
    else:
        print("not a palindrome")