def investment_val(amt, rate, years):
    num_months=years*12.0
    mon_int_rate=rate/1200
    futureInvestmentValue= amt * (1+mon_int_rate)**num_months
    return round(futureInvestmentValue,2)
print ( investment_val (1000 ,4.25 ,1) )
print ( investment_val (1500 ,3.25 ,2) )
print ( investment_val (1000 ,2.25 ,0.5) )
print ( investment_val (2000 ,4.25 ,3) )
