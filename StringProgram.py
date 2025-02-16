

# string are arrays in python and we can access the element of string using index
a="I love you baby and I can do anything for you priyu"
print(a[3])

# for currentChar in a:
#     print(currentChar)


#print length of string
print(len(a))

#check if string contains a word , it works similar to contains in java
print("love " in a)


if("priyu" in a):
    print("you are my love")
else :
    print("I stil love you more ")



#slicing of string
print(a[2:5]) #this will print lov
print(a[:5]) #this will print I lov
print(a[5:]) #this will print e you baby and I can do anything for you priyu
print(a[-5:]) #this will print priyu
print(a[-5:-2]) #this will print pri



