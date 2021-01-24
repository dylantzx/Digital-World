def minutes_to_years_days(minutes):
    days=minutes/1440
    years=days/365
    days_left=days%365
    return int(years),int(days_left)

print (minutes_to_years_days (1000000000))

print (minutes_to_years_days (2000000000))
