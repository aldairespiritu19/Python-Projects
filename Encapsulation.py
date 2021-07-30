




# Create protected class
class Protected:
    def __init__(self):
        self._protectedVar = 7


# Create object and prints the value
obj = Protected()
obj._varProtected = 6
print(obj._varProtected)


# Initialized function 
class Protected:
    def __init__(self):
        self.__privateVar = 19

        
    def getPrivate(self):
        print(self.__privateVar)
        

    def setPrivate(self, private):
        self.__privateVar = private



# Create object inhereted, returns the value
# and sets the private variable a new value
obj = Protected()
obj.getPrivate()
obj.setPrivate(10)
obj.getPrivate()

