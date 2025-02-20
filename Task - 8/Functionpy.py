#Question 1
# def greet(name):
#     print("Hello,"+ name)

# a = input("Enter Name :")
# greet(a)

#Question 2
# def add_num(a,b):
#     print(a+b)

# x = int(input("Enter the first num :"))
# y = int(input("Enter the second num : "))

# add_num(x,y)

#Question 3
# def is_even(n):
#     if n % 2 == 0:
#         print(True)
#     else:
#         print(False)

# a = int(input("Enter a num : "))
# is_even(a)

#Question 4
# def calculated_area(radius):
#     area = 3.141 * (radius*radius)
#     print(area)

# r = int(input("Enter the radius of Circle :  "))
# calculated_area(r)

#Question 5
# def find_max(a,b,c):
#     if a > b and b > c:
#         print(a , " is the Largest number ")
#     elif b > a and b > c:
#         print(b , " is the Largest number ")
#     else:
#         print(c , " is the Largest number ")

# x = int(input("Enter the First num : "))
# y =int(input("Enter the Second num : "))
# z = int(input("Enter the third num : "))

# find_max(x,y,z)

#Question 6
# def factorial(n):
#     num = 1
#     for i in range(2, n+1):
#         num *= i
#     print("Factorial : ", num )

# a = int(input("Enter a Number : "))
# factorial(a)

#Question 7
# def reverse_string(s):
#     print (s[::-1])

# a = input("Enter a String : ")
# reverse_string(a)

#Question 8
# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count = 0
#     for i in s:
#         if i in vowels:
#             count += 1
#     print("No.of vowels in this srting is",count)

# a = input("Enter a String : ")
# count_vowels(a)

#Question 9
# def is_palindrome(s):
#     c = s.lower()
#     r = c[::-1]
#     if c == r:
#         print("Is palindrome")
#     else:
#         print("Not a Palindrome")

# a = input("Enter a String : ")
# is_palindrome(a)

#Question 10
# def fab(n):
#     fib=[]
#     a =0
#     b=1
#     for i in range(n):
#         fib.append(a)
#         a,b = b,a+b
#     print(fib)

# x = int(input("Enter a Num: "))
# fab(x)

#Question 11
# def sum_of_list(lst):
#     sum = 0
#     for i in lst:
#         sum += i 
#     print(sum)

# x = int(input("Enter the limit of the list : "))
# y =[]

# for i in range(x):
#     num = int(input(f"Enter the number {i+1} : "))
#     y.append(num)

# sum_of_list(y)

#Question 12
# def find_largest(lst):
#     largest = 0
#     for i in lst:
#         if i > largest:
#             largest = i
#     print(f"largest number is {largest}")

# x = int(input("Enter the limit of the list : "))
# y =[]

# for i in range(x):
#     num = int(input(f"Enter the number {i+1} : "))
#     y.append(num)
# find_largest(y)

#Question 13
# def merge_list(lst1,lst2):
#     lst1.extend(lst2)
#     print(lst1)

# x = int(input("Enter the limit of first list : "))
# y =int(input("Enter the limit of the second list: "))
# s=[]
# r=[]

# for i in range(x):
#     num = int(input(f"Enter the number for first list : "))
#     s.append(num)
# for i in range(y):
#     num = int(input("Enter the number for the second list : "))
#     r.append(num)

# merge_list(s,r)

#Question 14
# def count_occurance(lst,element):
#     count = 0
#     for i in lst:
#         if i == element:
#             count += 1
#     print(f"the no of {element}'s in list is {count}")

# x = int(input("Enter the limit of the list : "))
# y =[]
# for i in range(x):
#     num = int(input(f"Enter the number {i+1} : "))
#     y.append(num)
# z= int(input("Enter the element to be counted : "))
# count_occurance(y,z)

#Question 15
# def is_prime(n):
#     if n < 2:
#         print("Is not a prime number")
#     elif n > 2:
#         for i in range(2,n):
#             if n % i == 0:
#                 print (f"{n} is not a prime number")
#                 return
#         print(f"{n} is a Prime number ")

# n = int(input("Enter a number : "))

# is_prime(n)

#Question 16
# def generate_multiplication_table(n,limit):
#     for i in range(1,limit+1):
#         print(f"{n} x {i} = {n*i}")

# n = int(input("Enter the number : "))
# limit = int(input("Enter the limit of the table : "))

# generate_multiplication_table(n,limit)

#Question 17
# def to_uppercase(s):
#     a = s.upper()
#     print(a)

# s = input("Enter a string : ")
# to_uppercase(s)

#Question 18
# def swap_values(a,b):
#     a,b=b,a
#     print(f"the first value is {a}")
#     print(f"the second value is {b}")

# x = input("Enter the first value : ")
# y = input("Enter the second value : ")

# swap_values(x,y)

#Question 19
# def remove_duplicates(lst):
#     s = set(lst)
#     print(list(s))

# x = int(input("Enter the limit of list : "))
# y =[]

# for i in range(x):
#     num = input(f"Enter the {i+1} of the list : ")
#     y.append(num)

# remove_duplicates(y)

#Question 20
# def calculate_power(base, exponent):
#     a = base ** exponent
#     print(f"the answer is: {a}")

# x = int(input("Enter the base : "))
# y = int(input("Enter the exponent : "))
# calculate_power(x,y)