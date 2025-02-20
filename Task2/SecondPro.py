#Question 1

#N = int(input('Enter the Number: '))

#for i in range(1,N+1):
 #   print(i)


#Question 2

#N = int(input('Enter the num: '))

#for i in range(2,N+1,2):
 #   print(i)

#Question 3    

#N=int(input('Enter The num: '))
#Sum = 0

#or i in range(1,N+1):
 #   Sum += i
#print('Total',Sum)


#Question 4

#N = int(input('Enter a Number: '))

#for i in range(1, 11):
#    print(f"{N} x {i} = {N * i}")


#Question 5

#string = input("Enter a String: ")
#reverseString = ""

#for i in string:
 #   reverseString = i + reverseString
#print('The Reverse is :', reverseString)


#Question 6

#N = int(input('Enter the Num: '))
#factorial = 1
#for i in range(1,N+1):
 #   factorial *= i
#print(f"Factorial of {N} is {factorial}" )


#Question 7

#N = int(input('Enter the number: '))


#if N < 2:
#    print("The number is not a Prime Number")
#else :
#      flag =True  
#      for i in range(2,N):
#              if N % i == 0:
#                    flag = False
#                    break
#      if flag:
#            print("Prime")
#      else:
#            print('Not a Prime')



#Question 8

#string = input('Enter a String :')
#vowels = 'aeiouAEIOU'
#consonant = 'bcdfghjklmnpqrtsvwxyzBCDFGHJKLMNPQRSTVWXYZ'

#vowels_count = consonant_count = 0

#for i in string:
    #if i in vowels:
   #     vowels_count += 1
  #  elif i in consonant:
 #       consonant_count += 1
#print('Vowels: ',vowels_count, ' Consonant: ', consonant_count)            

#Question 9
#N = int(input('Enter a limit: '))
#a= 0
#b = 1

#for i in range(N):
#    print(a)
#    a,b=b,a+b



#Question 10

#N = int(input('Enter no.of Rows: '))

#for i in range(1,N+1):
 #   print('*' * i)


#Question 11
# N = int(input('Enter a number: '))
# count = 0

# while N > 0:
#     N //= 10
#     count += 1
# print('Number of Digits :', count)

#Question  12

#N = input('Enter a Number: ')
#sum = 0

#for i in N:
  #  if int(i )>= 0 and int(i) <= 9:
 #       sum += int(i)
#print("Sum of digits : ", sum)


#Question 13
#N=input('Enter a string : ')
#d = ''

#for i in N:
#    d = i+d
#if(N==d):
#    print('Is Palindrome')
#else:
#    print('Not a Palindrome')    



#Question 14






#Question 15

#N = int(input('Enter a Number: '))
#square = 0
#for i in range(1,N+1):
#    square = i * i
#    print(f"{i} = {square}")