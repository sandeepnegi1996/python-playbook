# string methods    
a="I love you baby and I can do anything for you priyu"
print(a.upper()) #this will print the string in upper case
print(a.lower())    #this will print the string in lower case
print(a.replace("baby","Darling")) #this will replace the word baby with priyu


#split and store in a list  
split_list = a.split(" ")
print(split_list[1]) 



print(a.capitalize())   #this will capitalize the first letter of string
print(a.casefold())     #this will convert the string to lower case
print(a.center(10))    #this will center the string in 100 character
print(a.count("u"))     #this will count the number of a in string


print(a.encode())       #this will encode the string


print(a.endswith("u"))  #this will return true if string ends with u
# print(a.find("baby"))   #this will return the index of baby in string
# print(a.index("baby"))  #this will return the index of baby in string
# print(a.isalnum())      #this will return true if string is alphanumeric
# print(a.isalpha())      #this will return true if string is alphabet
# print(a.isascii())  # Return True if all characters in the string are ASCII, otherwise False.

# print(a.isdecimal())    #this will return true if string is decimal
# print(a.isdigit())      #this will return true if string is digit
# print(a.isidentifier()) #this will return true if string is identifier
# print(a.islower())      #this will return true if string is lower
# print(a.isnumeric())    #this will return true if string is numeric
# print(a.isprintable())  #this will return true if string is printable
# print(a.isspace())      #this will return true if string is space
# print(a.istitle())      #this will return true if string is title
# print(a.isupper())      #this will return true if string is upper   
# print(a.join("baby"))   #this will join the string with baby



# easiet way to format the string in python 

age=23
print(f"My name is sandeep and my age is { age*10 }")
print(f"My name is sandeep and my age is { age:.2f}")
print(f"My name is sandeep and my age is { age*10 }")



#escape character in string backslash so that we can inlcude quotes in the string 
print("I love you so much \"priyu\"   ")