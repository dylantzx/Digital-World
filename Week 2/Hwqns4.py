def wind_chill_temp(temp,speed):
    t_wc=35.74+0.6215*temp-35.75*speed**0.16+0.4275*temp*speed**0.16
    return t_wc
print ( wind_chill_temp (5.3 ,6) )

print ( wind_chill_temp (2.2 ,4) )
