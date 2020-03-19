from math import pi

class Lingkaran:
    def __init__(self,radius):
        self.radius=radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self, radius):
        return self.radius
    
    def hitungLuas(self):
        return pi * (self.radius ** 2)
    def hitungKeliling(self):
        return 2*pi*self.radius