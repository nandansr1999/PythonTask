#Question1
# task =[5,10,15,20,25]
# print(task[0],task[-1])

#Question2
# task = [1,2,3,4,5]
# task[1]=10
# print(task[1])

#Question3
# task=[1,2,3,4,5]
# task.insert(5,6)
# print(task)

#Question4
# task=[1,2,3,4,5]
# task.pop(2)
# print(task)

#Question5
# task=[1,2,3,4,5]
# print(len(task))

#Question6
# task=[1,2,3,4,5]
# reverseTask = task[::-1]
# print(reverseTask)

#Question7
# task=[5,10,15,20]
# if 10 in task:
#     print('Yes, 10 is there in the list')
# else:
#     print('No, 10 is not there in the list')

#Question 8
# task1= [1,2,3]
# task2 =[4,5,6]
# task3= task1 + task2
# print(task3)

#Question 9
# task=[1,2,3,4,5]
# newTask=[x*x for x in task]
# print(newTask)

#Question 10
# task=[4,7,1,9,3]
# task.sort()
# print(f"Minimum value is {task[0]} and Maximum Value is {task[-1]}")

#Question 11
# task=[1,2,3,4,5]
# total=0
# for x in task:
#     total += x
# print(total)

#Question 12
# task1 = [1,2,3]
# task2 = [3,2,1]

# task1.sort()
# task2.sort()
# if task1 == task2:
#     print("yes they are equal")
# else:
#     print("they are not equal")

#Question 13
# task1 =[1,2,3]
# task2 = [4,5,6]
# task1.extend(task2)
# print(task1)

#Question 14
# task = [1,2,2,3,4,2]
# count = 0
# for x  in task:
#     if x ==2:
#         count += 1
# print (count)

#Question 15

# task = [1,2,3,4,5]
# print(task.index(5))

#Question 16
# task = [1,2,3,4,5]
# newTask = [x for x in task if x > 3]
# print(newTask)

#Question 17
# task = [1,2,3,4,5]
# task = [x for x in task if x<=3]
# print(task)

#Question 18
task = [5,3,8,1,4]

for i in range(len(task)):
    for j in range(i + 1, len(task)):
        if task[i] > task[j]:
            task[i],task[j] = task[j],task[i]
print(task)



#Question 19
# task = [10,20,30,40,50]
# task.sort(reverse=True)
# print(task[1])
