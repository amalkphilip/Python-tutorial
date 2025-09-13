#Author : Amal k philip
#Description : Odd indexed and Even indexed charaters in the String.
    s = input("Enter the String :")
    even_chars = ''
    odd_chars = ''
    
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]
    
    print(f"{even_chars} {odd_chars}")



"""
Input : hello

Output : hlo el
"""
