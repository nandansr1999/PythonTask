#Question 1
# s = {4,7,1,9,3}
# l =list(s)
# max = l[0]
# min = l[0]

# for i in s:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max,min) 

#Question 2

# l = [1,2,2,3,4,4,5]
# s = set()

# for i in l:
#     if i not in s:
#         s.add(i)
# print(s)

#Question 3

# l = {1,3,5,7,9}
# emp = True

# for i in l:
#     emp = False
# print("Empty : ", emp)

#Question 4

# s = {2,4,6,8}
# count = 0

# for i in s:
#     count += 1
# print("Count: ",count)

#Question 5

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# s3 = set()

# for i in s1:
#     if i not in s2:
#         s3.add(i)
# for i in s2:
#     if i not in s1:
#         s3.add(i)

# print(s3)


#Question 6

# s1= {2,4,6}
# s2 = {1,2,3,4}
# s3 = set()

# for i in s1:
#     s3.add(i)
# for i in s2:
#     s3.add(i)
# print(s3)

#Question 7

# s = {2,4,6,8}
# l=list(s)

# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]
# print(l)


#Question 8

# s={10,20,30,40}
# l = list(s)

# for i in l:
#     s.remove(i)
# print(s)

#Question 9

# s ={1,2,3}
# t = ()

# for i in s:
#     t += (i,)
# print(t)


#Question 10

# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7}
# s1,s2 = s2,s1
# print(s1,s2)

#Question 11

# s={2,4,6,8,10}
# sum=0

# for i in s:
#     sum += i
# print(sum)