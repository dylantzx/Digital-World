class Time:
    def __init__(self, hours, mins, secs):
        self._hours = hours
        self._minutes = mins
        self._seconds = secs

    def getter(self):
        sec_hr = self._hours *3600
        sec_min = self._minutes * 60
        sec_total = sec_hr + sec_min + self._seconds
        return sec_total
    
    def setter(self, value):
        secs_in_day = 24*3600
        if value > secs_in_day:
            remain_sec = value % secs_in_day
        else:
            remain_sec = value
            
        num_hours = remain_sec//3600
        num_mins = (remain_sec - num_hours*3600)//60
        num_secs = (remain_sec - num_hours*3600)%60
        #print( num_hours, num_mins, num_secs)
        self._hours = num_hours
        self._minutes = num_mins
        self._seconds = num_secs
        

    def __str__(self):
        return "Time: {}:{}:{}".format(self._hours, self._minutes, self._seconds)
    
    elapsed_time = property(getter, setter)
        

t= Time(10, 19, 10)
print(t.elapsed_time)
t.elapsed_time = 555550
print(t.elapsed_time)
print(t)
