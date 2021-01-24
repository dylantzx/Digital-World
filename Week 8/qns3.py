import time

class StopWatch:
    def __init__(self):
        self._starttime = time.time()
        self._endtime = -1
        
    def start(self):
        self._starttime= time.time()
        self._endtime = -1
    
    def stop(self):
        self._endtime = time.time()
    
    def elapsed_time(self):
        if self._endtime == -1:
            return None
        else:
            return round(self._endtime-self._starttime,1)
            #return round(time.time()-self._starttime,1)
    

sw = StopWatch()
time.sleep(0.1)
sw.stop()
print(sw.elapsed_time())
sw.start()
time.sleep(0.2)
print(sw.elapsed_time())
sw.stop()
print(sw.elapsed_time())

