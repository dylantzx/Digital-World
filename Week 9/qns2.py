import libdw.sm as sm

class SimpleAccount(sm.SM):
    def __init__(self, balance):
        self.start_state = balance

    def get_next_values(self, state, inp):
        #Do not modify the state by using self.state = state, self.state = next_state

        
        if state < 100 and inp <0:
            next_state = state + inp -5
            output = next_state
        else:
            next_state = state + inp
            output = next_state

        return next_state, output
    
acct = SimpleAccount(110)
acct.start()
print(acct.transduce([10,-25,-10,-5,20,20]))
