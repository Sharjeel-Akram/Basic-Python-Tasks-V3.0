# Write a Python program to get unique values from a list.
# Sample Input: [10,15,20,10,30,35,20]
# Expected Output: [10,15,20,30,35]
def unique(List):
    unique_List=[]
    for i in List:
        if i not in (unique_List):
            unique_List.append(i)
    return unique_List


List = []
Limit_List= int(input("enter the limit of your list: "))
print("Enter your Number for list: ")
for i in range(int(Limit_List)):
    number = int(input(" "))
    List.append(number)
print("the original list which you input: ",List)
print("the unique value from the list is: ", unique(List))

