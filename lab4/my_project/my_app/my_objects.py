class Vehicle:
    def __init__(self, year, make, model, color, sound):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.sound = sound

    def honk(self):
        return self._sound
    
    @property 
    def wheels(self):
        return self._wheels
    








class Car(Vehicle):
    def __init__ (self, color, sound, make, model, year):
        super().__init__(year, make, model, color, sound)
         
        
        
        self._wheels = 4

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year, color, sound)

        self._wheels = 2



    
    
   



