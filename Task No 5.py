# Write a Python program which takes numbers as input and stores them in a list. Then
# converts the list into a single integer.
# Sample Input: [12,1,39]
# Expected Output: 12139



List = []
Limit_List = int(input("Enter the Limit of your list please: "))
print("Enter the numbers for List: ")
for i in range(int(Limit_List)):
    Numbers = int(input(" "))
    List.append(Numbers)
print("The Original List which you input is: ")
print(List)
Single_integer = List[0]
for i in range(1, len(List)):
    Single_integer = str(Single_integer) + str(List[i])
Single_integer = int(Single_integer)
print("The Single Integer Which You Got: ", Single_integer)




                               # USING BUILT IN FUNTION



# Write a Python program which takes numbers as input and stores them in a list. Then
# converts the list into a single integer.
# Sample Input: [12,1,39]
# Expected Output: 12139


List = []
Limit_List = int(input("Enter the Limit of your list please: "))
print("Enter the numbers for List: ")
for i in range(int(Limit_List)):
    Numbers = int(input(" "))
    List.append(Numbers)
print("The Original List which you input is: ")
print(List)
for i in List:
    print(i, end= '')
