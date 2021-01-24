from Qns2 import *


def display_calendar_modified(year, month):

    if month == None:
        return display_calendar(year)
    elif month >= 1 or month <= 12:
        return construct_month(year, month)
    

def construct_month(year, month):
    cal_month = construct_cal_year(year)
    output = ""
    output += cal_month[month][0] + "\n"
    output += "  S  M  T  W  T  F  S\n"
    for week in cal_month[month][1:]:
        output += week + "\n"
    return output[:-1]

def print_space_display_calendar_modified(calendar):
    temp=calendar.replace(' ', '*')
    return temp.replace('\n', '+\n')

out = display_calendar_modified(2020,11)
#print(print_space_display_calendar_modified(out))
print(out)


