class WeekDayError(Exception):
    pass

class Weeker:
    valid_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.valid_days:
            raise WeekDayError

        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        pass

    def subtract_days(self, n):
        pass

if __name__ == "__main__":
    try:
        weekday = Weeker('Mon')
        print(weekday)
        # weekday.add_days(15)
        # print(weekday)
        # weekday.subtract_days(23)
        # print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")
