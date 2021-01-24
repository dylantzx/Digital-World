class Celsius:
    def __init__(self,temperature=0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return self._temperature*9/5+32

    def get_temperature(self):
        return self._temperature
        
    def set_temperature(self, value):
        if value < -273:
            self._temperature = -273
        else:
            self._temperature = value
        #no need to return because this is just setting. I do not want to get the value
        #A setter is a measure to filter what you want.
    
    temperature = property(get_temperature, set_temperature) # no bracket because you do not want to call the methods but just associate then function with the property
    #What is inside property defines which function to look at
    #get and set is important in programming. 

c = Celsius()
print(c.temperature)

c = Celsius()
c.temperature = 32
print(c.to_fahrenheit())

c = Celsius()
c.temperature= -300
print(c.temperature)

c = Celsius(-300)
print(c.get_temperature())

c=Celsius()
c.set_temperature(20)
print(c.temperature)
