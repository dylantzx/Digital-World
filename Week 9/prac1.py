class SM:

    def __init__(self):
        self.state = None

    def start(self): #self points to object instance
        self.state = self.start_state
        
    def step(self,inp):
        #move machine to next state based on input
        state = self.state
        ns, out = self.get_next_values(state, inp) #ns for next state, out for output
        self.state = ns
        return out
        
    def get_next_values(self, state, inp):
        pass
    
class LightBox(SM):
        start_state = "OFF"
        
        def get_next_values(self, state, inp):
            if state == "ON":
                if inp == 1:
                    next_state = "OFF"
                    output = 0
                else:
                    next_state = "ON"
                    output = 1
            else:
                if inp == 1:
                    next_state = "ON"
                    output = 1
                else:
                    next_state = "OFF"
                    output = 0
            
            return next_state, output
        
lb = LightBox() #Object instantiation
print(lb.state)
lb.start()
print(lb.state)
print(lb.step(1))
print(lb.step(1))
print(lb.step(1))
print(lb.step(0))
print(lb.step(1))

