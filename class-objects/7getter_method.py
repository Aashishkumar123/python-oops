'''
Getter method is an instance method in python class which is used to get the value.
We use prefix get to define the getter method 
'''


class Car(object):
    def __init__(self, capcity, engine) -> None:    # constructor
        self.capacity = capcity                     # instance variable
        self.engine = engine

    def get_features(self):                         # getter method
        print(f'The feature of this car has {self.capacity} sitting capacity and a powerful {self.engine} engine.')   # body


obj = Car(4,'v501')
obj.get_features()