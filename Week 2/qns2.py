def bmi(weight, height):
    height /= 100
    result = weight/ (height**2)
    return round(result, 1)
print(bmi(60,120))
print(bmi(50,150))
print(bmi(43.5,142.3))
print(bmi(95.5,180))
