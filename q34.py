# Python program to convert given string into another case. If the string is in uppercase, convert to lowercase and vice-versa

str1 = "haha"
str2 = "HAHA"

def herapheri (str):
    if(str.isupper()):
        return str.lower()
    else:
        return str.upper()
        
print(herapheri(str1))
print(herapheri(str2))
