# Example of a birthday calculator using python.

from datetime import datetime, timedelta

class Birthday:
    def __init__(self, birth_date):
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        if today < self.birth_date.replace(year=today.year):
            age -= 1
        return age

    def time_until_next_birthday(self):
        today = datetime.today()
        next_birthday = self.birth_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        remaining_time = next_birthday - today
        return remaining_time

# Input from user
birth_date = input("Enter your birthday (YYYY-MM-DD): ")
person = Birthday(birth_date)

print("Your age:", person.calculate_age())
time_left = person.time_until_next_birthday()
print("Time until next birthday:", time_left.days, "days,", time_left.seconds // 3600, "hours,",
      (time_left.seconds // 60) % 60, "minutes, and", time_left.seconds % 60, "seconds")