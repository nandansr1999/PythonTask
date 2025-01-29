#Question 1
a = int(input('Enter The first Number: '))
b= int(input('Enter The Second Number: '))
c = int(input('Enter The Third Number: '))

if a > b and a > c :
    print(f"{a} is the Largest number")
elif b > a and b > c:
    print(f"{b} is the Largest Number")
else:
    print(f"{c} is the largest number")


#Question 2

year = int(input('Enter the Year: '))

if year % 4 == 0 and year % 100 != 0 :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#Question 3

num = int(input('Enter a Number: '))

if num >= 1 and num <= 10:
    print('Small')
elif num >= 11 and num <= 20:
    print("Medium")
elif num > 20:
    print('Large')
else:
    print("Enter a Positive Number")



#Question 4

temp = float(input('Enter the temperature: '))

if temp < 0:
    print('Cold')
elif temp >= 0 and temp <= 15:
    print('Cool')
elif temp >= 16 and temp <=30:
    print ('Warm')
elif temp > 30:
    print('Hot')
else:
    print('Enter a Valid number')


#Question 5

bmi = float(input('Enter the BMI:  '))

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <=24.9:
    print("Normal weight")
elif bmi >= 25 and bmi <=29.9:
    print("Over weight")
elif bmi >= 30:
    print("Obese")
else:
    print('Enter a Vaid BMI')



#Question 6 

color = input('Choose a Color from Red , Yellow or Green: ')

if color == 'Red' or color == 'red':
    print("Stop")
elif color == 'Yellow' or color == 'yellow':
    print("Get Ready")
elif color == 'Green' or color == 'green':
    print("Go")
else:
    print("Invalid Color")


#Question 7

char = input('Enter a Character')
vowels = 'AEIOUaeiou'
conso = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

if char in vowels:
    print('The Character is a Vowel')
elif char in conso:
    print('The Character is a Consonant')
else:
    print('Enter a valid Character')



#Question 8 

Num = int(input('Enter a number: '))

if Num % 2 == 0 and Num % 3 == 0:
    print('Divisible by both 2 and 3')
elif Num % 2 == 0:
    print('Divisible by  2 ')
elif Num % 3 == 0:
    print('Divisible by  3 ')
else:
    print('Not divisible by 2 and 3')





#Question 9 

Multi = int(input('Enter a number: '))

if Multi % 5 == 0 or Multi % 7 == 0:
    print('The number is a multiple of 5 or 7')
else:
    print('The number is not a multiple of 5 or 7')



# Question 10

age = int(input('Enter the age: '))

if age >= 17:
    print('R')
elif age >= 13:
    print('PG-13')
elif age >= 8:
    print('PG')
else:
    print('G')

