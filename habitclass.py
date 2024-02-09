import datetime
from database import mycursor, mydb


"""
Initialises the class Habit so that Habit objects can be created
"""


class Habit:

    def __init__(self, name: str, periodicity: str, current_streak=0, longest_streak=0):
        self.name = name
        self.periodicity = periodicity
        self.start_date = datetime.date.today().strftime('%Y-%m-%d')
        self.current_streak = current_streak
        self.longest_streak = longest_streak

# inserts information into the database when a user creates new habits
    def insert_to_db(self):
        mycursor.execute('INSERT INTO current_habits '
                         '(HabitName, Periodicity, HabitStart, CurrentStreak, LongestStreak) '
                         'VALUES (%s,%s,%s,%s,%s)', (self.name, self.periodicity,
                                                     self.start_date, self.current_streak, self.longest_streak))
        mydb.commit()


"""
Enables user to create their own daily habit and adds that habit to the database
"""


def add_daily_habit(habit_name):
    new_habit = Habit(habit_name, "Daily")
    new_habit.insert_to_db()


"""
Enables user to create their own weekly habit and adds that habit to the database
"""


def add_weekly_habit(habit_name):
    new_habit = Habit(habit_name, "Weekly")
    new_habit.insert_to_db()
