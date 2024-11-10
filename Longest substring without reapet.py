"""
Author:Amal k philip
Date:10-11-2024
Description: the length of the string without repeating characters.

 
"""


stri=input("enter a string without space:")
lis=[]
Count=0
y=""
n=len(stri)
for i in range(0,n):
    if stri[i] not in y:
        y=y+stri[i]
        
        Count=Count+1
        

print("The length of string:",Count)
print("The Answer is","\"",y,"\"")
