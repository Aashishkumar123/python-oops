'''
Class method are just like a normal functions but has little difference.
It take first argument as a cls.
To create a class method, we use @classmethod decorator just above the method.
class method is used to access the class or static variable.
'''

# CLASS METHOD WITHOUT PARAMETER

class Car(object):
    GEAR = 'Manual'           # class or static variable

    @classmethod                       # decorator
    def show(cls):                      # class method
        print(f'Gear is {cls.GEAR}')    # accessing the class or static variable


Car().show()      # by class you can call the class method, don't need to create object




# CLASS METHOD WITH PARAMETER

class Car(object):
    GEAR = 'Manual'           # class or static variable

    @classmethod                       # decorator
    def show(cls, capacity):
        cls.capacity = capacity                      # class method
        print(f'Gear is {cls.GEAR} and capacity is {cls.capacity}')    # accessing the class or static variable


Car().show(5)      # by class you can call the class method and pass the required argument to show method
