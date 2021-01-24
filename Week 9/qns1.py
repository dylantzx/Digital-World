#from libdw.sm import SM
import libdw.sm as sm

#class CM(SM):
class CM(sm.SM):
        start_state = 0
        
        def get_next_values(self, state, inp):
            if state == 0:
                if inp == 100:
                    next_state = 0
                    output = (0, "coke", 0)
                elif inp == 50:
                    next_state = 1
                    output = (50, "--", 0)
                else:
                    next_state = 0
                    output = (0, "--" , inp)
            else:
                if inp == 100:
                    next_state = 0
                    output = (0, "coke", 50)
                elif inp == 50:
                    next_state = 0
                    output = (0, "coke", 0)
                else:
                    next_state = 1
                    output = (50, "--", inp)
            
            return next_state, output
        
cm = CM() #Object instantiation
#transduce: 1) will call start 2) step() for all inp into the list
#output a list
print(cm.transduce([100, 50, 50, 10, 50, 80, 100]))
"""
cm.start()
print(cm.state)
print(cm.step(100))
print(cm.step(50))
print(cm.step(50))
print(cm.step(10))
print(cm.step(50))
print(cm.step(80))
print(cm.step(100))
"""
