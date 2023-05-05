class Timer:
    def __init__(hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:0d}""

    def next_second(self):
        pass

    def prev_second(self):
        pass

if __name__ == "__main__":
    timer = Timer(23, 59, 59)
    print(timer) # 23:59:59
    timer.next_second()
    print(timer) # 00:00:00
    timer.prev_second()
    print(timer) # 23:59:59
