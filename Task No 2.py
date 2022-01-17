# Write a Python program which takes two lists as input and then prints the common 
# values.
# Sample input: 
# list1= [10,20,30,40,50]
# list2= [30,40,60,70]
# Expected Output= [30,40]
List1 = []
Limit_List1 = int(input("Enter the limit of List1: "))
print("Enter the numbers for List1: ")
for i in range(int(Limit_List1)):
    Numbers = int(input(" "))
    List1.append(Numbers)
List2 = []
Limit_List2 = int(input("Enter the limit of List2: "))
print("Enter the numbers for List2: ")
for i in range(int(Limit_List2)):
    Numbers = int(input(" "))
    List2.append(Numbers)
Common_List = []
for i in List1:
    if i in List2:
        Common_List.append(i) 
print("List1 is : ", List1)
print("List2 is : ", List2)
print("So the Commmon Numbers From List1 and List2 is : ", Common_List)