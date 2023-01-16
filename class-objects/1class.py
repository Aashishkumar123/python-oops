'''
Class is creating using class keyword with class name where first character always be a capital letter and it inherit 
the object class by default but if you don't specify that's fine.
'''

class Car(object):          # empty python class
    pass



'''
A class is blueprint or a template that basically encapsulate all the business logics with in a class.
It holds the instant, class or static variables and instance, class, static method.
'''


obj = Car()               # creating class object or reference



'''
When we define any class using class keyword, the memory is not intialized in private heap memory.
When we create an object or reference of a class then the memory is intialized in private heap memory.
And we can create mutiple objects or reference of a single class.
'''