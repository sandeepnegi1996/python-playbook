
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# main data types in python are    list,tuple,dict,bool


listExample = [1,2,3] #this is list example , list is mutable , we can change the value of list,    listExample[0] = 4 #this will change the value of listExample to [4,2,3]
tupleExample = (1,2,3) #this is tuple example 
dictExample = {"name":"sandeep","age":30} #this is dictionary exampl
isAgeGreaterThan18 = True #this is boolean example



print(listExample)
print(tupleExample)
print(dictExample)
print(isAgeGreaterThan18)


x =int(1)
y =float(2.3)
z = complex(2334343j)

print(type(x),type(y),type(z))


#type conversion

t =float(x)
print(t,type(t))


q=int(y)
print(q,type(q))



