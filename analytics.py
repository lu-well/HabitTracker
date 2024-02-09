import pandas
import warnings
from database import mycursor, mydb, habit_exists


"""
Library recommendation. Ensures there is no warning message displayed when the Pandas Dataframe is returned
"""

warnings.filterwarnings('ignore')


"""
Functions which check if there are any habits, daily habits, weekly habits in the database
"""


def check_if_no_habits():
    mycursor.execute('SELECT HabitName FROM current_habits')
    selectable_habits = mycursor.fetchall()
    if len(selectable_habits) == 0:
        return True
    else:
        return False


def check_if_no_daily_habits():
    mycursor.execute('SELECT HabitName FROM current_habits WHERE Periodicity = "Daily"')
    selectable_habits = mycursor.fetchall()
    if len(selectable_habits) == 0:
        return True
    else:
        return False


def check_if_no_weekly_habits():
    mycursor.execute('SELECT HabitName FROM current_habits WHERE Periodicity = "Weekly"')
    selectable_habits = mycursor.fetchall()
    if len(selectable_habits) == 0:
        return True
    else:
        return False


"""
Retrieves the names of all habits currently in the database
"""


def get_current_habits():
    mycursor.execute('SELECT HabitName FROM current_habits')
    selectable_habits = mycursor.fetchall()
    if len(selectable_habits) > 0:
        for i in selectable_habits:
            print(i[0])
    else:
        print("No habits available, please add a habit to proceed!")


"""
Retrieves the names of all daily habits currently in the database
"""


def get_daily_habits():
    mycursor.execute('SELECT HabitName FROM current_habits WHERE Periodicity = "Daily"')
    daily_habit_list = mycursor.fetchall()
    if len(daily_habit_list) > 0:
        for i in daily_habit_list:
            print(i[0])
    else:
        print("No daily habits available, please add a habit to proceed!")


"""
Retrieves the names of all weekly habits currently in the database
"""


def get_weekly_habits():
    mycursor.execute('SELECT HabitName FROM current_habits WHERE Periodicity = "Weekly"')
    weekly_habit_list = mycursor.fetchall()
    if len(weekly_habit_list) > 0:
        for i in weekly_habit_list:
            print(i[0])
    else:
        print("No weekly habits available, please add a habit to proceed!")


"""
Shows all habits which are currently tracked along with their current and longest streaks
"""


def all_habit_streaks():
    sql_query = pandas.read_sql('SELECT HabitName, CurrentStreak, LongestStreak FROM current_habits', mydb)
    df = pandas.DataFrame(sql_query)
    print(df.to_string(index=False))


"""
Returns current streak as integer
"""


def check_current_streak(habit_to_check):
    check_current = "SELECT CurrentStreak FROM current_habits WHERE HabitName = %s"
    mycursor.execute(check_current, (habit_to_check,))
    current_streak = mycursor.fetchall()
    return current_streak[0][0]


"""
Returns longest streak as integer
"""


def check_longest_streak(habit_to_check):
    check_longest = "SELECT LongestStreak FROM current_habits WHERE HabitName = %s"
    mycursor.execute(check_longest, (habit_to_check,))
    longest_streak = mycursor.fetchall()
    return longest_streak[0][0]


"""
Shows the streaks of a particular habit which the user inputs
"""


def specific_habit_streak():
    get_current_habits()
    habit_to_check = input("type the habit which you want to check: ")
    if habit_exists(habit_to_check):
        sql_query = pandas.read_sql('SELECT HabitName, CurrentStreak, LongestStreak '
                                    'FROM current_habits WHERE HabitName = %s', mydb, params=(habit_to_check,))
        df = pandas.DataFrame(sql_query)
        print(df.to_string(index=False))
    else:
        pass
