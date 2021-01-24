def describe_bmi(bmi):
    if bmi < 18.5:
        message = "nutritional deficiency"
    elif bmi >= 18.5 and bmi < 23:
        message = "low risk"
    elif bmi >= 23 and bmi < 27.5:
        message = "moderate risk"
    else:
        message = "high risk"
    return message

print(describe_bmi(18))
print(describe_bmi(18.5))
print(describe_bmi(20))
print(describe_bmi(23))
print(describe_bmi(27.5))
print(describe_bmi(30))





