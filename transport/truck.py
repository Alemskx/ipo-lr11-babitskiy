from .vehicle import *
class Truck(Vehicle):
    def __init__(self, capacity,color,):
        super().__init__(capacity,)
        try:
            color = str(color)
            self.color = color
        except:
            print("Цвет укаазывается строкой")