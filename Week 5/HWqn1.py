# NB: you do not need to submit the 'get_data' function

def extract_values(values):
    tup = tuple(map(int, values.split())) 
   
    return tup

def calc_ratios(values):
    if values[1] == 0:
        return None
    else:
        ratio = values[0]/values[1]
    return ratio

def get_data():
    int_pair = input("Enter integer pair (hit Enter to quit):\n")
    tup_val = extract_values(int_pair)
    ratio = calc_ratios(tup_val)
    return ratio

print(get_data())

