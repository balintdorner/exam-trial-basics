# Create a class that represents a cuboid:
# It should take its three dimensions as constructor parameters (numbers)
# It should have a method called `get_surface` that returns the cuboid's surface
# It should have a method called `get_volume` that returns the cuboid's volume

class Cuboid(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_surface(self):
        surface = 2 * (self.a * self.b + self.a * self.c + self.b * self.c)
        return surface

    def get_volume(self):
        volume = self.a * self.b * self.c
        return volume



box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
