class Polynomial(object):
    def __init__(self, coefficient_list):
        self.coeff = coefficient_list
        
    def __add__(self, other):
        if len(self.coeff) >= len(other.coeff):
            shorter_list = other.coeff
            longer_list = self.coeff
        else:
            shorter_list = self.coeff
            longer_list = other.coeff
            
        total_coeff = []
        for idx in range(len(shorter_list)):
            new_coeff = self.coeff[idx] + other.coeff[idx]
            total_coeff.append(new_coeff)
        total_coeff += longer_list[idx+1::] 
        return Polynomial(total_coeff)
        
    def __sub__(self, other):
        if len(self.coeff) >= len(other.coeff):
            shorter_list = other.coeff
            longer_list = self.coeff
        else:
            shorter_list = self.coeff
            longer_list = other.coeff
        remain_len = len(longer_list) - len(shorter_list)
        total_coeff = []
        remain_list = list(0 for a in range(remain_len))
        #print(remain_list)
        for idx in range(len(shorter_list)):
            new_coeff = self.coeff[idx] - other.coeff[idx]
            total_coeff.append(new_coeff)

        re_list = []
        
        for re_idx in range(len(remain_list)):
            
            if len(self.coeff[idx+1:]) !=0:
                re_num = self.coeff[idx+1:][re_idx]-remain_list[re_idx]
                
            else:
                re_num = remain_list[re_idx]-other.coeff[idx+1:][re_idx]
            re_list.append(re_num)
            
        #print(re_list)
        
        total_coeff += re_list
            
        return Polynomial(total_coeff)
    
    def __call__(self, x):
        value = 0
        for count in range(len(self.coeff)):
            value += self.coeff[count]*((x)**(count))
        return value
    
    def __mul__(self, other):
        if len(self.coeff) >= len(other.coeff):
            shorter_list = other.coeff
            longer_list = self.coeff
        else:
            shorter_list = self.coeff
            longer_list = other.coeff

        new_coeff = []
        newlistlength = len(shorter_list)+len(longer_list)-1
        for idx in range(len(shorter_list)):
            inner_list = []
            for idx1 in range(len(longer_list)):
                num = shorter_list[idx] * longer_list[idx1]
                inner_list.append(num)
            if idx == 0:
                inner_list+= [0 for i in range(newlistlength-len(longer_list))]
            else:
                #print(idx)
                #print(inner_list)
                inner_list= [0]*idx +inner_list 
                inner_list= inner_list + [0]*(len(longer_list)-idx-1)
                
            #print(inner_list)    
            new_coeff.append(inner_list)
            #print(new_coeff)
        total_coeff = list(0 for i in range(newlistlength))
        
        #print(newlistlength, total_coeff)
        for numtimes in range(len(new_coeff)):
            for times in range(newlistlength):
                #print(times, numtimes)
                #print(new_coeff[0][times], end=" ")
                total_coeff[times]+=new_coeff[numtimes][times]
        
        return Polynomial(total_coeff)
    
    def differentiate(self):
        new_coeff = []
        for count in range(1,len(self.coeff)):
            newcoeff = self.coeff[count]*(count)
            new_coeff.append(newcoeff)
        #print(new_coeff)
        self.coeff = new_coeff 
        return None
    
    def derivative(self):
        new_obj_coeff = []
        for count in range(1,len(self.coeff)):
            newobjcoeff = self.coeff[count]*(count)
            new_obj_coeff.append(newobjcoeff)
        newobj = Polynomial(new_obj_coeff)
        return newobj

"""
p = Polynomial([1, 2, 3])
q = Polynomial([2, 3])
r=p-q
print(r.coeff) #[-1, -1, 3]
r=q-p
print(r.coeff) #[1, 1, -3]  
"""
p1 = Polynomial([1, -1])
p2 = Polynomial([0, 1, 0, 0, -6, -1])
#p3 = p1 + p2
#print(p3.coeff) #[1, 0, 0, 0, -6, -1]

p4 = p1*p2
print(p4.coeff) #[0, 1, -1, 0, -6, 5, 1]

"""
p2 = Polynomial([0, 1, 0, 0, -6, -1])
p5 = p2.derivative()
print(p5.coeff) #[1, 0, 0, -24, -5]
   

p = Polynomial([1,3,5,7,9])
p.differentiate()
print(p.coeff) #[3, 10, 21, 36]

p = Polynomial([1,-2,0,0,6,1])
print(p(3))
"""

p1 = Polynomial([1, 2 ,3, 4])
p2 = Polynomial([1, 2 ,3, 4])
p3 = p1*p2
print(p3.coeff) #[1, 4, 10, 20, 25, 24, 16]
