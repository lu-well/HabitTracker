# Habit Tracker App

This app allows users to add habits to their profile from a pre-defined list or create their own habits,  
complete their habits and analyse their habit streaks.

## What does it do?

The habit tracker opens with the main menu, which prompts the user to select which action 
they want. "Add Habit" allows the user to choose to add either a daily or weekly habit, and 
they can either insert their own habit, or choose from the pre-defined habits. "Complete 
Habit" allows the user to check their habit and stores this data to calculate the habit 
streak. If the user does not complete the habit in the corresponding required time period 
(daily/weekly), the streak is broken and is reset. Streaks can be viewed in "Analyse 
Habits" which provides information on the current streak and also the longest streak for 
each habit. Users can also "Delete Habit" when they no longer want a habit on their 
profile. 

## Installation

```shell
pip install -r requirements.txt
```

## Usage

Start

```shell
python main.py 
```

This opens the home page of the app, and depending on the option selected will take the 
user down the path to complete the action. Once this is done, the app returns again to the 
home screen until the user selects "Exit", then the program stops.

## Tests

```shell
pytest .
```
