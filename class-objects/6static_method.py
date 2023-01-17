'''
Static method are just like a normal functions.
It don't take any default argument just like instance method and class method.
To create a static method, we use @staticmethod decorator just above the method.
Static method is used when processing is related to class only but no need of any class object.
'''

# STATIC METHOD WITHOUT PARAMETER

class Car(object):

    @staticmethod        # decorator
    def show():          # static method  
        print('staticmethod called')   # body of static method

Car().show()              # call static method using class don't need to create an object



# STATIC METHOD WITH PARAMETER

class Car(object):

    @staticmethod        # decorator
    def show(music_system,):          # static method  
        print(f'music system - {music_system}')   # body of static method

Car().show('Dolby music')              # call static method using class and pass the required arguments in show method
