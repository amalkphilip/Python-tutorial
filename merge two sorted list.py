"""
Author:Amal K Philip
Description:the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

#list 1
list1=input("Enter the numbers for list 1 with space:")
list1=list1.split()
main_list1=[]
for i in list1:
    i=int(i)
    main_list1.append(i)

#list 2
list2=input("Enter the numbers for list 2 with space:")
list2=list2.split()
main_list2=[]
for i in list2:
    i=int(i)
    main_list2.append(i)

#final list
main_list=main_list2+main_list1
main_list.sort()
print(main_list)
