

# this is the parent class with attributes 
class Person:
    name = 'No Name Provided'
    email = ''
    password = 'abc000'
    account_number = 1


# this is the child class number 1 with their own attributes
class Player(Person):
    salary = 50,000,000.00
    championships = '3'


# child class number 2 with their own attributes
class Coach(Person):
    years_experience = '10'
    age = '65'
