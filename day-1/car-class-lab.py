# Andela labs car class lab


class Car(object):
    """A Car object."""

    speed = 0

    def __init__(self, name='General', model="GM", car_type="saloon"):
        self.name = name
        self.model = model
        self.type = car_type
        if self.name in ('Koenigsegg', 'Porshe'):
          self.num_of_doors = 2
        else: self.num_of_doors = 4
        if self.type == 'saloon':
          self.num_of_wheels = 4
        else: self.num_of_wheels = 8

    def is_saloon(self):
        return self.type == 'saloon'

    def drive(self, speed):
        if self.name == 'MAN':
            self.speed = 77
        else:
            self.speed = 10 ** speed
        return self