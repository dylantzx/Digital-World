def compound_value_months(amt, annual_int, n):
    value = 0
    mon_int = annual_int/12
    for i in range(n):
        value = (amt+value)*(1+mon_int)
    return round(value,2)
ans = compound_value_months(100, 0.05 , 6)
print(ans)
ans = compound_value_months(100, 0.03 , 7)
print(ans)
ans = compound_value_months(200, 0.05 , 8)
print(ans)
ans = compound_value_months(200, 0.03 , 1)
print(ans)
