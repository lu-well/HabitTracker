import pytest
from habitclass import add_daily_habit, add_weekly_habit
from database import *
from analytics import *


"""
Creates table and runs tests for main functionalities of the program
"""


class TestHabit:

    create_table()

    def setup_method(self):
        self.test_table = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='PandaMySQL1992!',
                    port='3306',
                    database='habit_tracker'
                    )
    mycursor = mydb.cursor(buffered=True)
    add_daily_habit("Drink 2l of water")
    add_daily_habit("Exercise for 20 minutes")
    add_daily_habit("Read for 15 minutes")
    add_weekly_habit("Clean apartment")
    add_weekly_habit("Plan calendar")

    def test_habit_exists(self):
        assert habit_exists("Drink 2l of water") is True

    def test_check_if_daily(self):
        assert check_if_daily("Exercise for 20 minutes") is True

# Mimics 4 weeks of completions and then tests whether streaks have been correctly recorded

    def test_increment_streak(self):
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Drink 2l of water")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        increment_streak("Exercise for 20 minutes")
        override_longest_streak("Exercise for 20 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        reset_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        increment_streak("Read for 15 minutes")
        override_longest_streak("Read for 15 minutes")
        increment_streak("Plan calendar")
        increment_streak("Plan calendar")
        increment_streak("Plan calendar")
        increment_streak("Plan calendar")
        increment_streak("Clean apartment")
        increment_streak("Clean apartment")
        increment_streak("Clean apartment")
        increment_streak("Clean apartment")
        override_longest_streak("Clean apartment")

    def test_checking_streaks(self):
        assert check_longest_streak("Exercise for 20 minutes") == 28
        assert check_longest_streak("Read for 15 minutes") == 11
        assert check_current_streak("Drink 2l of water") == 28
        assert check_current_streak("Plan calendar") == 4
        assert check_longest_streak("Clean apartment") == 4

    def test_update_completion(self):
        update_completion("2024-05-02", "Clean apartment")
        assert check_last_completion("Clean apartment") == "2024-05-02"

    def test_reset_streak(self):
        reset_streak("Clean apartment")
        assert check_current_streak("Clean apartment") == 1

    def test_delete_habit(self):
        delete_habit("Drink 2l of water")
        delete_habit("Exercise for 20 minutes")
        delete_habit("Read for 15 minutes")
        delete_habit("Clean apartment")
        delete_habit("Plan calendar")
        assert habit_exists("Plan calendar") is False

    def teardown_method(self):
        pass
