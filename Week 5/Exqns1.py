def move_disks(n, fromTower, toTower, auxTower, sol):
    lst=[fromTower, toTower, auxTower]
    if n>0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move_disks(n-1, fromTower, toTower, auxTower, sol)
        
        string = "Move disk {} from {} to {}".format(n, lst[n-1],lst[n])
        sol.append(string)
        move_disks(n+1, fromTower, toTower, auxTower, sol)
        return sol
        string = "Move disk {} from {} to {}".format(n+1, lst[n-1],lst[n+1])
        sol.append(string)
        string = "Move disk {} from {} to {}".format(n, lst[n],lst[n+1])
        sol.append(string)
        string = "Move disk {} from {} to {}".format(n, lst[n-3],lst[n-2])
        sol.append(string)
        """
        
        
       
        string = "Move disk {} from {} to {}".format(n-2, lst[n-1],lst[n-3])
        sol.append(string)
        string = "Move disk {} from {} to {}".format(n-1, lst[n-1],lst[n-2])
        sol.append(string)
        string = "Move disk {} from {} to {}".format(n-2, lst[n-3],lst[n-2])
        sol.append(string)

        
        move_disks(n-1, fromTower, toTower, auxTower, sol)
        

        print(lst,lst1,lst2, '############', sep = '\n')

        move_disks(n-1,auxTower,toTower, fromTower , sol)
   
   
    sol.append(string)
    #string = move_disks(n, fromTower, toTower, auxTower, sol)
    return sol"""


sol = []
move_disks(1,'A','B','C',sol)
print(sol) #1 from A to B
"""
sol = []
move_disks(3,'A','B','C',sol)
print(sol) #1 from A to B, 2 from A to C, 1 from B to C, 3 from A to B
            # 1 from C to A, 2 from c to B, 1 from A to B


"""
