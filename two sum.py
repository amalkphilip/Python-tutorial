"""
Author:Amal k philip
Date:10-11-2024
Description:Location of elements in a list if sum is obtain
"""

lis=[]
n=int(input("enter no: Elements:"))
while n>0:
    num=int(input("enter the element:"))
    lis.append(num)
    n=n-1

target=int(input("Enter the sum of two element:"))
counta=0
sumb=0
print("the Elements:",lis)
for i in lis:
    countb=0
    for k in lis:
        
        sumb=int(i+k)
        if target==sumb:
            print("the location of elements:","[",counta,",",countb,"]")
        countb+=1
    counta+=1