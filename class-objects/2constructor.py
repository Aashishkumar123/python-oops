'''
A constructor is a special method used in class, that automatically calls when we create an object of class.
A constructor is also used to instialize the instant variable.
To define a contructor in class we use __init__(self) method. 
'''

# CONSTRUCTOR WITHOUT PARAMETER

class Car(object):
    def __init__(self) -> None:          # constructor
        print(self)
        print('Constructor called......')


obj1 = Car()                            # first object of a class
obj2 = Car()                            # second object of class


# METHODS

'''
A method is just like a function but it is little bit different from a normal function.
A method takes a first argument always a self and it always define inside a class.
'''


# SELF

'''
A self is a keyword in python, that holds the address of current object of a class.
You must have to pass self as a first parameter in any method in class, otherwise it raise an exception.
'''


# CONSTRUCTOR WITH PARAMETER

class Car(object):
    def __init__(self, model) -> None:          # constructor with parameter
        self.model = model                      # instant variable
        print('Constructor called......')


obj = Car('xyz')                            # object of a class


'''
When you are creating a parameterize constructor, you must have to pass the argument to the class while creating its object.
'''
