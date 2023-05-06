class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def next_second(self):
        seconds = (self.__seconds + 1) % 60
        minutes_adj = (self.__seconds + 1) // 60
        minutes = (self.__minutes + minutes_adj) % 60
        hours_adj = (self.__minutes + minutes_adj) // 60
        self.__hours = (self.__hours + hours_adj) % 24
        self.__minutes = minutes
        self.__seconds = seconds

    def prev_second(self):
        seconds = 59 if self.__seconds == 0 else self.__seconds - 1 
        minutes_adj = 1 if self.__seconds == 0 else 0
        self.__seconds = seconds
        if minutes_adj == 0:
            return
        
        minutes = 59 if self.__minutes == 0 else self.__minutes - 1
        hours_adj = 1 if self.__minutes == 0 else 0
        self.__minutes = minutes        
        if hours_adj == 0:
            return
        
        self.__hours = 23 if self.__hours == 0 else self.__hours - 1
        
if __name__ == "__main__":
    timer = Timer(23, 59, 59)
    print(timer) # 23:59:59
    timer.next_second()
    print(timer) # 00:00:00
    timer.prev_second()
    print(timer) # 23:59:59
    timer.prev_second()
    print(timer) # 23:59:58
