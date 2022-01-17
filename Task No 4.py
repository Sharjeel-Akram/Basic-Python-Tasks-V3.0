# Write a Python program which takes a list as input and then changes the position of every 
# n
# th value with the (n+1)th in a list.
# Sample list: [10,20,30,40,50,60] 
# Expected Output: [20, 10, 40, 30, 60, 50]



def Change_Position(Org_List):
    for i in range(0,len(Org_List),2):
        Org_List[i],Org_List[i+1]=Org_List[i+1],Org_List[i]
    return Org_List


Org_List = []
Limit_List = int(input("Enter the limit of your List Please: "))
print("Enter The numbers of your List: ")
for i in range(int(Limit_List)):
    Numbers = int(input(""))
    Org_List.append(Numbers)
print("Original List which you input is: ")
print(Org_List)
print("After Changing the position the list is: ")
print(Change_Position(Org_List))