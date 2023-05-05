class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def next_second(self):
        seconds = (self.__seconds + 1) % 60
        add_minutes = (self.__seconds + 1) // 60
        minutes = (self.__minutes + add_minutes) % 60
        add_hours = (self.__minutes + add_minutes) // 60
        self.__hours = (self.__hours + add_hours) % 24
        self.__minutes = minutes
        self.__seconds = seconds

    def prev_second(self):
        pass

if __name__ == "__main__":
    timer = Timer(23, 59, 59)
    print(timer) # 23:59:59
    timer.next_second()
    print(timer) # 00:00:00
    # timer.prev_second()
    # print(timer) # 23:59:59
