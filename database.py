"""
Database module used to input, store data and return queries
"""
import mysql.connector
import datetime
from datetime import datetime
from datetime import timedelta


"""
Connects to database
"""


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='PandaMySQL1992!',
    port='3306',
    database='habit_tracker'
    )

mycursor = mydb.cursor(buffered=True)


"""
Creates table if it is not already created
"""


def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS current_habits ("
                        "HabitName varchar(255),"
                        "Periodicity varchar(255),"
                        "HabitStart varchar(255),"
                        "MostRecentCompletion varchar(255),"
                        "CurrentStreak int,"
                        "LongestStreak int"
                        ");")


"""
Checks if a habit exists within the database, if it doesn't will return an error message
"""


def habit_exists(chosen_habit):

    mycursor.execute('SELECT HabitName FROM current_habits')
    tuple_list = mycursor.fetchall()
    str_list = []
    for Tuple in tuple_list:
        str_list.append(Tuple[0])
    if chosen_habit not in str_list:
        print("I didn't recognise that habit, please check the spelling and try again!")
        return False
    else:
        return True


"""
Removes the chosen habit from the database
"""


def delete_habit(chosen_habit):
    remove_habit = "DELETE FROM current_habits WHERE HabitName = %s"
    mycursor.execute(remove_habit, (chosen_habit,))
    mydb.commit()
    print(f"your habit {chosen_habit} was deleted!")


"""
Resets the current streak to 0 when a habit streak has been broken
"""


def reset_streak(chosen_habit):
    start_streak_again = "UPDATE current_habits SET CurrentStreak = 1 WHERE HabitName = %s"
    mycursor.execute(start_streak_again, (chosen_habit,))
    mydb.commit()


"""
Allows user to complete their chosen habit, or shows error message if it is too early to complete it
"""


def complete_habit():
    chosen_habit = input("Type the name of the habit from the above list which you want to complete: ")
    if habit_exists(chosen_habit):
        if check_if_daily(chosen_habit):
            last_daily_completion(chosen_habit)
        else:
            last_weekly_completion(chosen_habit)
    else:
        pass


"""
Updates the date when a habit has been completed
"""


def update_completion(today, chosen_habit):
    update_last_date = "UPDATE current_habits SET MostRecentCompletion = %s WHERE HabitName = %s"
    mycursor.execute(update_last_date, (today, chosen_habit))
    mydb.commit()


"""
Checks if a habit has daily listed as the periodicity
"""


def check_if_daily(chosen_habit):
    if habit_exists(chosen_habit):
        mycursor.execute("SELECT Periodicity from current_habits WHERE HabitName = %s", (chosen_habit,))
        periodicity = mycursor.fetchall()
        str_list = []
        for Tuple in periodicity:
            str_list.append(Tuple[0])
        if "Daily" not in str_list:
            return False
        else:
            return True


"""
Takes the most recent completion date from the database and compares it to today's date.
If no previous completion this is treated as the first completion. If the user tries to complete
the habit on the same day as the last completion it shows a message that it is too early. If the
user completes their daily habit the day after the last completion, it shows that the habit was
completed and they added to their streak. If the date is any other date it shows that the user
has completed their habit but broken their streak
"""


def last_daily_completion(chosen_habit):
    today = datetime.today().strftime('%Y-%m-%d')
    mycursor.execute("SELECT MostRecentCompletion from current_habits WHERE HabitName = %s", (chosen_habit,))
    most_recent = mycursor.fetchall()
    if most_recent == [(None,)]:
        update_completion(today, chosen_habit)
        increment_streak(chosen_habit)
        override_longest_streak(chosen_habit)
        print("Habit completed!")
    else:
        str_list = []
        for Tuple in most_recent:
            str_list.append(Tuple[0])
        converted_most_recent = ''.join(str_list)
        reconverted_date = datetime.strptime(converted_most_recent, "%Y-%m-%d")
        last_completion_date = reconverted_date.strftime("%Y-%m-%d")
        yesterday = datetime.today() - timedelta(days=1)
        converted_yesterday = yesterday.strftime('%Y-%m-%d')
        if last_completion_date == today:
            print("It's too early to complete this habit, try again later")
        elif last_completion_date == converted_yesterday:
            update_completion(today, chosen_habit)
            increment_streak(chosen_habit)
            override_longest_streak(chosen_habit)
            print("Habit completed! You have added to your streak!")
        else:
            update_completion(today, chosen_habit)
            reset_streak(chosen_habit)
            print("Habit completed! Unfortunately you broke your streak.")


"""
Takes the most recent completion date from the database and compares it to today's date.
If no previous completion this is treated as the first completion. If the user tries to complete
the habit within less than a week of the last completion it shows a message that it is too early.
If the user completes their weekly habit the week after the last completion, it shows that the 
habit was completed and they added to their streak. If the date is any other date it shows that 
the user has completed their habit but broken their streak
"""


def last_weekly_completion(chosen_habit):
    today = datetime.today().strftime('%Y-%m-%d')
    mycursor.execute("SELECT MostRecentCompletion from current_habits WHERE HabitName = %s", (chosen_habit,))
    most_recent = mycursor.fetchall()
    if most_recent == [(None,)]:
        update_completion(today, chosen_habit)
        increment_streak(chosen_habit)
        override_longest_streak(chosen_habit)
        print("Habit completed!")
    else:
        str_list = []
        for Tuple in most_recent:
            str_list.append(Tuple[0])
        converted_most_recent = ''.join(str_list)
        reconverted_date = datetime.strptime(converted_most_recent, "%Y-%m-%d")
        last_completion_date = reconverted_date.strftime("%Y-%m-%d")
        last_week = datetime.today() - timedelta(days=7)
        converted_last_week = last_week.strftime('%Y-%m-%d')
        if last_completion_date > converted_last_week:
            print("It's too early to complete this habit, try again later")
        elif last_completion_date == converted_last_week:
            update_completion(today, chosen_habit)
            increment_streak(chosen_habit)
            override_longest_streak(chosen_habit)
            print("Habit completed! You have added to your streak!")
        else:
            update_completion(today, chosen_habit)
            reset_streak(chosen_habit)
            print("Habit completed! Unfortunately you broke your streak.")


"""
Updates the current streak of the chosen habit by incrementing the current streak value by 1
"""


def increment_streak(chosen_habit):
    add_to_current = "UPDATE current_habits SET CurrentStreak = CurrentStreak + 1 WHERE HabitName = %s"
    mycursor.execute(add_to_current, (chosen_habit,))
    mydb.commit()


"""
Compares the current streak of the chosen habit to the longest streak and replaces the longest
streak if the current streak exceeds the incumbent longest streak, otherwise does nothing
"""


def override_longest_streak(chosen_habit):
    mycursor.execute("SELECT CurrentStreak from current_habits WHERE HabitName = %s", (chosen_habit,))
    current_streak = mycursor.fetchall()
    mycursor.execute("SELECT LongestStreak from current_habits WHERE HabitName = %s", (chosen_habit,))
    longest_streak = mycursor.fetchall()
    if longest_streak <= current_streak:
        replace_longest = "UPDATE current_habits SET LongestStreak = CurrentStreak WHERE HabitName = %s"
        mycursor.execute(replace_longest, (chosen_habit,))
        mydb.commit()
    else:
        pass


def change_date():
    yesterday = datetime.today() - timedelta(days=1)
    converted_yesterday = yesterday.strftime('%Y-%m-%d')
    chosen_habit = input("Type: ")
    update_last_date = "UPDATE current_habits SET MostRecentCompletion = %s WHERE HabitName = %s"
    mycursor.execute(update_last_date, (converted_yesterday, chosen_habit))
    mydb.commit()


def check_last_completion(chosen_habit):
    mycursor.execute("SELECT MostRecentCompletion from current_habits WHERE HabitName = %s", (chosen_habit,))
    most_recent = mycursor.fetchall()
    str_list = []
    for Tuple in most_recent:
        str_list.append(Tuple[0])
    converted_most_recent = ''.join(str_list)
    reconverted_date = datetime.strptime(converted_most_recent, "%Y-%m-%d")
    last_completion_date = reconverted_date.strftime("%Y-%m-%d")
    return last_completion_date
