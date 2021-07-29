



# Parent Class Drink
class Drink:
    name = "unknown"
    color = "yellow"
    size = "12oz"
    available = True


    # Method for Parent Class
    def getInfo(self):
        entry_name = input("Enter drink name: ")
        entry_size = input("Enter drink size: ")
        if (entry_name == "unknown" and entry_size == "12oz"):
            print("Drink is available!")
        else:
            print("Sorry, drink not available!")


# Child Class Drink
class Soda(Drink):
    name = "sprite"
    color = "clear"
    size = "12oz"
    calories = "140"
    sugar = "38g"
    available = True


    # This is the same method in the Parent Class
    # Difference is it's using entry_sugar
    def getInfo(self):
        entry_name = input("Enter drink name: ")
        entry_sugar = input("Enter drink sugar: ")
        if (entry_name == "sprite" and entry_sugar == "38g"):
            print("Drink is available!")
        else:
            print("Sorry, drink not available!")


# Child Class Drink
class Coffee(Drink):
    name = "latte"
    color = "brown"
    size = "12oz"
    temperature = "hot"
    origin = "italy"
    available = True


    # This is the same method in the Parent Class
    # Difference is it's using entry_origin
    def getInfo(self):
        entry_name = input("Enter drink name: ")
        entry_origin = input("Enter drink origin: ")
        if (entry_name == "latte" and entry_origin == "italy"):
            print("Drink is available!")
        else:
            print("Sorry, drink not available!")


# This code invokes the methods in each class
beverage = Drink()
beverage.getInfo()

soda = Soda()
soda.getInfo()

coffee = Coffee()
coffee.getInfo()
    
