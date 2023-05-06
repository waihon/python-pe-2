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
        day_n = Weeker.valid_days.index(self.__day)
        day_n = (day_n + n) % 7
        self.__day = Weeker.valid_days[day_n]

    def subtract_days(self, n):
        day_n = Weeker.valid_days.index(self.__day)
        day_n = (day_n - n) % 7
        self.__day = Weeker.valid_days[day_n]

if __name__ == "__main__":
    try:
        weekday = Weeker('Mon')
        print(weekday)             # Mon
        weekday.add_days(15)
        print(weekday)             # Tue
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday') # Sorry, I can't serve your request.
    except WeekDayError:
        print("Sorry, I can't serve your request.")
