'''
Instance method are just like a normal functions but has little difference.
It take first argument as a self.
Instance method is used to access the instance variable.
'''


class Car(object):
    def __init__(self, m, c) -> None:           # constructor with parameter
        self.model = m                          # instant variable
        self.color = c                          # instant variable
    
    def show(self):                                                     # instant method
        print(f'model : {self.model} , color : {self.color}')           # access instant variable


obj = Car('xuv','black')                     # create class object
obj.show()                                   # call instant method


obj1 = Car('suv','white')                     # create class object
obj1.show()                                   # call instant method


Car('xuv','black').show()                   # you can also call through class but not recommended way