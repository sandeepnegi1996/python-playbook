# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)


my_list1 = [1,2,3,3,4,"sandy",True]
print(my_list1[2])

#insert element in the list 
# by inserting element in the list, it will shift the element to the right side.
my_list.insert(3,"sandy")
print(my_list)

#append element in the list
my_list.append("priyu")
print(my_list)

# #remove element from the list
my_list.remove(1)
print(my_list)




# #pop element from the list
my_list.pop()
print(my_list)

my_list.append("priyu")
print(my_list)

# #del element from the list
del my_list[1]
print(my_list)

# #clear the list
my_list.clear()
print(my_list)



#combine two list in python using extend , we can also extend the list using + operator and we can add other collection like tuple,dict etc
list1 = ["a", "b" ,"b","c","c", "c"]
list2 = [1, 2, 3]
list1.extend(list2) #this will return None
print(list1) #this will print ['a', 'b', 'c', 1, 2, 3]


list1.pop(1)
print(list1) #this will print ['a', 'c', 1, 2, 3]

# list1.clear()
# print(list1) #this will print []


list1.remove("c")
print(list1) #this will print ['a', 1, 2, 3]

for x in list1:
    print(x)

print("===============================================")

for i in range(len(list1)):
    print(list1[i])





# Tuple unmutable -> we can not change the value of tuple once it is assigned amd hence it is faster than list
# my_tuple = (1, 2, 3, 4, 5)
# print("Tuple:", my_tuple)

# # Set
# my_set = {1, 2, 3, 4, 5}
# print("Set:", my_set)

# # Dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print("Dictionary:", my_dict)


# mutable -> but does not allow duplicate values basically the keys will be unique
car_dict = {
    "brand":"suzuki",
    "model":"swift",
    "year":2020,
    "seater":5
}

print(car_dict)

print(car_dict["brand"])
print(car_dict.get("model"))
print(car_dict.keys())
print(car_dict.values())
print(car_dict.items())








