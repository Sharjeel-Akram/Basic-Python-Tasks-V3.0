# Write a Python program to print all sub-lists of a list.
# Sample Input: [1,2,3]
# Expected Output: [ [], [1], [1,2], [1,2,3] [2], [2,3],[3]]

def Display_Sublists(Orig_List):
    Sub_List=[[]]
    for i in range(len(Orig_List)+1):
        for j in range(i+1, len(Orig_List)+1):
            Slicing_Numbers = Orig_List[i:j]
            Sub_List.append(Slicing_Numbers)
    return Sub_List


Orig_List=[]
Limit_List = int(input("Enter the Limit of your List please: "))
print("Enter the numbers for List: ")
for i in range(int(Limit_List)):
    Numbers = int(input(" "))
    Orig_List.append(Numbers)
print("The original List which you take as input is: ")
print(Orig_List)
print("The Sublists of Original List is: ")
print(Display_Sublists(Orig_List))