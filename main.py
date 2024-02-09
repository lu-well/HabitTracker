import questionary
import database
import analytics
import habitclass


"""
Enables user to add a habit and stores that habit in the database
"""


def add_habit():
    choice = questionary.select(
        "Do you want to add your own habit or a predefined habit?",
    choices=["my own habit", "a predefined habit"]
    ).ask()
    if choice == "my own habit":
        new_habit = input("Type the name of your new habit: ")
        choice = questionary.select(
            "which type of habit is this?",
            choices=["Daily Habit", "Weekly Habit"]
        ).ask()
        if choice == "Daily Habit":
            habitclass.add_daily_habit(new_habit)
        elif choice == "Weekly Habit":
            habitclass.add_weekly_habit(new_habit)
        print(f"your new habit {new_habit} has been added!")
    elif choice == "a predefined habit":
        choice = questionary.select(
            "choose a predefined habit to add",
            choices=["Drink 2l of water - Daily", "Exercise for 20 minutes - Daily",
                     "Read for 15 minutes - Daily", "Clean apartment - Weekly", "Plan calendar - "
                                                                                "Weekly"]
        ).ask()
        if choice == "Drink 2l of water - Daily":
            habitclass.add_daily_habit("Drink 2l of water")
            print("your new habit Drink 2l of water has been added!")
        elif choice == "Exercise for 20 minutes - Daily":
            habitclass.add_daily_habit("Exercise for 20 minutes")
            print("your new habit Exercise for 20 minutes has been added!")
        elif choice == "Read for 15 minutes - Daily":
            habitclass.add_daily_habit("Read for 15 minutes")
            print("your new habit Read for 15 minutes has been added!")
        elif choice == "Clean apartment - Weekly":
            habitclass.add_weekly_habit("Clean apartment")
            print("your new habit Clean apartment has been added!")
        elif choice == "Plan calendar - Weekly":
            habitclass.add_weekly_habit("Plan Calendar")
            print("your new habit Plan calendar has been added!")


"""
Enables the user to input the name of the habit they want to delete
"""


def delete_habit():
    if analytics.check_if_no_habits() is False:
        analytics.get_current_habits()
        chosen_habit = input("Enter the name of the habit from the above list which you want to delete: ")
        if database.habit_exists(chosen_habit):
            database.delete_habit(chosen_habit)
    else:
        questionary.press_any_key_to_continue("You don't currently have any habits! "
                                              "Press any key to return to the home page").ask()


"""
Begins the CLI for the user to complete all actions on the habit tracker app
"""


def cli():
    questionary.press_any_key_to_continue("Welcome to the habit tracker! Here you can add habits and complete "
                                          "them to build up your streaks. Remember that to keep up your streaks,"
                                          " daily "
                                          "habits must always be completed on subsequent days and weekly "
                                          "habits must be completed on the same weekday that you first complete"
                                          " the habit. You can "
                                          "analyse your streaks and remove habits whenever"
                                          " they are no longer applicable. Press any key to begin").ask()
    database.create_table()
    stop = False
    while not stop:
        choice = questionary.select(
            "what do you want to do?",
            choices=["Complete Habit", "Add Habit", "Delete Habit", "Analyse Habits", "Exit"]
        ).ask()

        if choice == "Add Habit":
            add_habit()

        elif choice == "Complete Habit":
            if analytics.check_if_no_habits() is False:
                analytics.get_current_habits()
                database.complete_habit()
            else:
                print("No habits available, please add a habit to proceed")
            questionary.press_any_key_to_continue(
                "Press any key to return to the home page"
            ).ask()

        elif choice == "Analyse Habits":
            choice = questionary.select(
                "what do you want to see?",
                choices=["List of daily habits", "List of weekly habits", "List of all habits",
                         "All habit streaks", "A specific habit streak"]
            ).ask()

            if choice == "List of daily habits":
                if analytics.check_if_no_daily_habits() is False:
                    analytics.get_daily_habits()
                    questionary.press_any_key_to_continue("These are your daily habits! "
                                                          "Press any key to return to the home page").ask()
                else:
                    questionary.press_any_key_to_continue("You don't currently have any daily habits! "
                                                          "Press any key to return to the home page").ask()

            elif choice == "List of weekly habits":
                if analytics.check_if_no_weekly_habits() is False:
                    analytics.get_weekly_habits()
                    questionary.press_any_key_to_continue("These are your weekly habits! "
                                                          "Press any key to return to the home page").ask()
                else:
                    questionary.press_any_key_to_continue("You don't currently have any weekly habits! "
                                                          "Press any key to return to the home page").ask()
            elif choice == "List of all habits":
                if analytics.check_if_no_habits() is False:
                    analytics.get_current_habits()
                    questionary.press_any_key_to_continue(
                        "These are all your habits! Press any key to return to the home page").ask()
                else:
                    questionary.press_any_key_to_continue("You don't currently have any habits! "
                                                          "Press any key to return to the home page").ask()
            elif choice == "All habit streaks":
                if analytics.check_if_no_habits() is False:
                    analytics.all_habit_streaks()
                    questionary.press_any_key_to_continue(
                        "These are all your habit streaks! Press any key to return to the home page").ask()
                else:
                    questionary.press_any_key_to_continue("You don't currently have any habits! "
                                                          "Press any key to return to the home page").ask()
            elif choice == "A specific habit streak":
                analytics.specific_habit_streak()
                questionary.press_any_key_to_continue(
                    "These are the streaks for your chosen habit! Press any key to return to the home page").ask()

        elif choice == "Delete Habit":
            delete_habit()

        elif choice == "Exit":
            print("Bye!")
            stop = True


if __name__ == '__main__':
    cli()
