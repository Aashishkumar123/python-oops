'''
A nested class is normal python class but it define inside the class.
A normal python can have more than one nested class.
'''


class Car(object):
    def __init__(self, color, engine) -> None:
        self.meta = self.Meta(color, engine)
        self.meta.show_details()

    class Meta:
        def __init__(self, color, engine) -> None:
            self.color = color
            self.engine = engine
        
        def show_details(self):
            print(f'color is {self.color} and engine is {self.engine}')

obj = Car('black','v501')
