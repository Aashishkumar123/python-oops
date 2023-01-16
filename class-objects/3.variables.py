'''
                                In python class we have two types of variable : 

                                            1. Instance variable

                                            2. Class variable
                                                                                                                                                    '''


# INSTANCE VARIABLE

'''
An instance variable are those variable whose seperate copy is created for every object.
And within a constructor we define an instance variable.
And to use instance variable we create instance method.
'''


class Car(object):                    
    def __init__(self,model) -> None:              # constructor
        self.model = model                         # instance variable


obj = Car('xcr')                             # object
print(obj.model)                             # call instance variable using object
print(id(obj.model))                         # print address of that instance variable


obj1 = Car('ydf')                             # object
print(obj1.model)                             # call instance variable using object
print(id(obj1.model))                         # print address of that instance variable


obj = Car('xcr')                             # object
obj.model = 'sks'                            # now we can also change the value of instance variable by its object now it return 'sks'
print(obj.model)                             # call instance variable using object
print(id(obj.model))                         # print address of that instance variable


obj1 = Car('ydf')                             # object
obj.model = 'ssl'                            # now we can also change the value of instance variable by its object now it return 'ssl'
print(obj1.model)                             # call instance variable using object
print(id(obj1.model))                         # print address of that instance variable



# CLASS VARIABLE

'''
A class variable are those variable whose one copy is created for every object.
And within a class we define an class variable.
And to use class variable we create class method.
'''


class Car(object):
    GEAR = 'Manual'                         # class variable

    def __init__(self) -> None:
        pass


print(Car.GEAR)                            # we can call class varaiable by the class name

obj = Car()                                # object
print(obj.GEAR)                            # we can also call class variable by its object
print(id(obj.GEAR))                        # printing id 

obj1 = Car()                               # object
print(obj1.GEAR)                           # we can also call class variable by its object
print(id(obj1.GEAR))                       # printing id 

Car.GEAR = 'Automatic'                     # we can change class variable by its class and it will change for every object. now you get the result 'Automatic'

obj = Car()                                # object
print(obj.GEAR)                            # we can also call class variable by its object
print(id(obj.GEAR))                        # printing id 

obj1 = Car()                               # object
print(obj1.GEAR)                           # we can also call class variable by its object
print(id(obj1.GEAR))                       # printing id 


obj.GEAR = 'Manual'                        # You can also change class variable for particular object. now you get the result 'Manual'
print(obj.GEAR)                            # we can also call class variable by its object
print(id(obj.GEAR))                        # printing id 


obj1 = Car()                               # object
print(obj1.GEAR)                           # we can also call class variable by its object
print(id(obj1.GEAR))                       # printing id 