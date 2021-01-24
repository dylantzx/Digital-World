import libdw.sm as sm

class CommentsSM(sm.SM):
    
    start_state = None
    
    def get_next_values(self, state, inp):
        if state == None:
            #print(state, inp)
            if inp == "#":
                output = inp
                next_state = "met"
            else:
                output = state
                next_state = state
        else:
            #print(state, inp)
            if inp == "\n":
                output = None
                next_state = None
            else:
                output = inp
                next_state = "met"            
        
        return next_state, output

Str = "def f(x): # comment\n return 1"
m = CommentsSM()
print(m.transduce(Str))
