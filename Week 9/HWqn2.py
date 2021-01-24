import libdw.sm as sm

class FirstWordSM(sm.SM):

    start_state = "new"

    def get_next_values(self, state, inp):
        if state == "new":
            if inp == " ":
                next_state = state
                output = None
                
            elif inp == "\n":
                output = None
                next_state = "new"
                
            else:
                output = inp
                next_state = "old"

        elif state == "old":
            if inp == "\n":
                next_state = state
                output = None
                
            elif inp == " ":
                next_state = "notfirst"
                output = None
                
            else:
                output = inp
                next_state = state
    
        else:
            if inp == "\n":
                next_state = "new"
                output = None
            else:
                next_state = state
                output = None

            

        return next_state, output

Str = "def f(x): # comment\n return 1"
m = FirstWordSM()
print(m.transduce(Str)) 

