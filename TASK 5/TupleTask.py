#Question1
# t = (1,2,3,4,5)
# print( (t[-1],) + t[1:-1] + (t[0],))

#Question 2
# x = (1,2,3,4,5)
# y = list(x)
# y.reverse()
# x = tuple(y)
# print(x)

#Question 3
# t = (4,5,7,3,8)
# maxTup = t[0]
# minTup = t[0]

# for i in t:
#     if i > maxTup:
#         maxTup = i
#     if i < minTup:
#         minTup = i
# print("Max :", maxTup , "Min :",minTup)

#Question 4
# t = (1,2,3,4,5)

# if len(t) == 0:
#     print("TUple is Empty")
# else:
#     print("Tuple is not Empty")


#Question 5
# s = "NANDAN"
# t=tuple(s)
# print(t)

#Questionn 6
# s = input("Enter a String seperated by Single Space : ")
# x = s.split()
# t = ()
# for i in x:
#     t += (i,)
# print(t)

#Question7 
# t = (1,2,3,4,5)
# sum = 0
# for i in t:
#     sum += i
# print(sum)


#Question 8

# t1 = (1,2,3,4,5,6)
# t2 = (6,7,8,9,10,11)
# result  = ()

# for i in t1:
#     for j in t2:
#         if i == j :
#             result += (i,)
# print(result)

#Question 9

# t = (1,2,3,4,5,6)
# even = []
# odd = []

# for i in range (len(t)):
#     if i % 2 == 0:
#         even.append(t[i])
#     else:
#         odd.append(t[i])
# print("Even :",even,"Odd",odd)

#Question 10
# t = (1,2,3,4,5,6,7,8,9,10)
# even = ()
# for i in t:
#     if i % 2 == 0:
#         even += (i,)
# print(even)


