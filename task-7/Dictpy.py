#Question 1
thisdict = {
    "Type" : "Hatchback",
    "Brand": "Renault",
    "Car": "Kwid",
    "Year" : 2017,
    "Owner": "Jimmy"
}

# print(thisdict)

#Question2

# print(thisdict["Type"])

#Question3
# flag = False
# for i in thisdict:
#     if i == "Owner":
#         flag = True
#         break
# if flag:
#     print("Key exists")
# else:
#     print("Key does not exists")


#Question4
# thisdict["Year"]= 2016
# print(thisdict)

#Question 5
# thisdict["Reg"]= "kerala"
# print(thisdict)

#Question 6
# newDi={}
# for i in thisdict:
#     if i != "Owner" :
#         newDi[i]=thisdict[i]
# print(newDi)

#Question 7
# for i in thisdict:
#     print(i)

#Question 8
# for i in thisdict:
#     print(thisdict[i])

#Question9
# for i in thisdict:
#     print(i, thisdict[i])

#Question 10
# thatdict = {
#     "OnwerType" : "Single Owner",
#     "Service" : 8 ,
#     "Accidental History" : "No"
# }

# output = dict(**thisdict,**thatdict)

# print(output)