'''
Setter method is an instance method in python class which is used to set the value.
We use prefix set to define the setter method 
'''


class Car(object):
    def set_feature(self, capcity, engine) -> None:    # setter method
        self.capacity = capcity                     # we are settting the value here
        self.engine = engine

    def get_features(self):                         # getter method
        print(f'The feature of this car has {self.capacity} sitting capacity and a powerful {self.engine} engine.')   # body


obj = Car()                                             # object
obj.set_feature(5,'v501')                               # calling the setter method
obj.get_features()                                      # calling the getter method
