# creation function


z=12 #global variable since it is declared outside the function scope can be accessed any where in the program 
# create simple function to print hello world and call it 
def printVariable():
    z=13 #local variable since it is declared inside the function scope can be accessed only inside the function
    print(z)


printVariable()



def printGlobalVariable():
    print("this will print hte global variable since there is no variable with the same name in the function scope")
    print(z)


printGlobalVariable()


# use global keyword and change the value inside a function 
age=12

def getAge():
    global age
    age=19
    print(age)


getAge()