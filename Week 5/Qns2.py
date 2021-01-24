def leap_year(year):
    div_by_4 = year%4==0 #the == changes it to a boolean and store as variable
    div_by_100 = year%100==0 #the == changes it to a boolean
    div_by_400 = year%400==0 #the == changes it to a boolean 

    if not div_by_4:
        return False

    elif not div_by_100:
        return True
    
    elif not div_by_400:
        return False
    
    else:
        return True

def day_of_week_jan1(year):
    q = 5*((year-1)%4)
    s = 4*((year-1)%100)
    t =6*((year-1)%400)
    p= (1+ q + s + t)
    d = p%7
    return d

def num_days_in_month(month_num, leap_year):

    mthdict = {1:31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if month_num == 2 and leap_year:
        return 29
    else:
        return mthdict.get(month_num, "Invalid Month")


def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month_name_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    output = [month_name_dict[month_num]]
    week = " " *first_day_of_month*3
    day = first_day_of_month
    date = 1
    while date <= num_days_in_month:
        while day <= 6:
            week+="{:3d}".format(date)
            date+=1 
            day+=1
            if date > num_days_in_month:
                break
        output.append(week)
        
        week = ""
        day = 0
                        
    return output

def construct_cal_year(year):
    output = [year]
    fdm = day_of_week_jan1(year)
    for mth in range(1,13):
        num_days = num_days_in_month(mth,leap_year(year))
        month_list = construct_cal_month(mth, fdm, num_days)
        fdm = (fdm + num_days)%7
        output.append(month_list)

    return output

def display_calendar(year):
    calendar = construct_cal_year(year)
    output = ""
    for mth_list in calendar[1:]:
        output += mth_list[0] + "\n"
        output += "  S  M  T  W  T  F  S\n"
        for week in mth_list[1:]:
            output+=week + "\n"
        output+= "\n"
    return output[:-2]   

"""def print_space_display_calendar(calendar):
    temp=calendar.replace(' ', '*')
    return temp.replace('\n', '+\n')"""

out = display_calendar(2020)
#print("START")
#print(print_space_display_calendar(out))
print(out)
#print("END")

