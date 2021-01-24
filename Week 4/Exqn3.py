import random as rnd

def throw_dice(n,nExp):
    prob = 0
    for exp in range(nExp):
        count = 0
        for num in range(n):
            dice_num = rnd.randint(1,6)
            print(dice_num)
            if dice_num == 6:
                count +=1
                prob += count/(num+1)
                break
        print("end of exp")
    prob /= nExp
    return round(prob,2)

print(throw_dice(3,2))
