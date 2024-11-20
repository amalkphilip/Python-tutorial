element=list(input("enter the character:"))
integer=['-','0','1','2','3','4','5','6','7','8','9']
newinteger=''
for char in element:
    if char not in integer:
        break
    else:
        newinteger=newinteger+char
newinteger=int(newinteger)

print(newinteger)
    