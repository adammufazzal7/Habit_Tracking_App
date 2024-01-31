import json
from datetime import datetime

class HabitTracker:
    def __init__(self):
        self.allHabits = {"daily": {}, "weekly": {}}
        self.loadHabitData()

    def loadHabitData(self):
        try:
            with open("habit_data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                self.allHabits.update(data)
        except FileNotFoundError:
            pass

    def addHabit(self, habitName, dailyWeekly):
        habitDict = self.allHabits[dailyWeekly]
        if habitName not in habitDict:
            habitDict[habitName] = []
            print(f"{habitName} has been added to the {dailyWeekly} list ")
        else:
            print(f"{habitName} is already present ")

    def removeHabit(self, habitName, dailyWeekly):
        habitDict = self.allHabits[dailyWeekly]
        if habitName in habitDict:
            del habitDict[habitName]
            print(f"{habitName} has been removed from the {dailyWeekly} list ")
        else:
            print(f"{habitName} not found ")

    def markHabit(self, habitName, date, dailyWeekly):
        habitDict = self.allHabits[dailyWeekly]
        if habitName in habitDict:
            if date not in habitDict[habitName]:
                habitDict[habitName].append(date)
                print(f"{habitName} has been marked for {date} ")
            else:
                print(f"{habitName} already marked for {date} ")
        else:
            print(f"{habitName} not found")

    def calculate_longest_streak(self, habit_dates):
        #habit_dates.sort()

        current_streak = 0
        longest_streak = 0
        current_date = None

        for date_str in habit_dates:
            date = datetime.strptime(date_str, "%d/%m/%y")

            if current_date is None or (date - current_date).days == 1:
                current_streak += 1
            else:
                current_streak = 1

            if current_streak > longest_streak:
                longest_streak = current_streak

            current_date = date

        return longest_streak


habitTracker = HabitTracker()

while True:
    print("\nHabit Tracker")
    print("1. Add a habit")
    print("2. Remove a habit")
    print("3. Mark a habit")
    print("4. Exit")

    choice = input("\nEnter your choice ")

    if choice == "1":
        dailyWeekly = input("Enter daily or weekly ")
        habitName = input("Enter your habit ")
        habitTracker.addHabit(habitName, dailyWeekly)

    elif choice == "2":
        dailyWeekly = input("Enter daily or weekly ")
        habitName = input("Remove your habit ")
        habitTracker.removeHabit(habitName, dailyWeekly)

    elif choice == "3":
        dailyWeekly = input("Enter daily or weekly ")
        habitName = input("Enter a habit you want to mark ")
        date = datetime.now().strftime("%d-%m-%Y")
        habitTracker.markHabit(habitName, date, dailyWeekly)

    elif choice == "4":
        with open("habit_data.json", "w") as jsonFile:
            json.dump(habitTracker.allHabits, jsonFile)
        break

    else:
        print("Enter 1, 2, 3, 4")

while True:
    print("\nHabit Tracker Data: ")
    print("1. List of all currently tracked habits")
    print("2. List of all habits with the same periodicity")
    print("3. Longest running streak of all habits")
    print("4. Longest running streak of a given habit")
    print("5. Exit")

    choice1 = input("Enter your choice ")

    if choice1 == "1":
        for dailyWeekly, habits in habitTracker.allHabits.items():
            for habit, dates in habits.items():
                print(f"{dailyWeekly.capitalize()} habit {habit}: {', '.join(dates)}")

    elif choice1 == "2":
        for dailyWeekly, habits in habitTracker.allHabits.items():
            for habit, dates in habits.items():
                print(f"{dailyWeekly.capitalize()} habit {habit}: {', '.join(dates)}")

    elif choice1 == "3":
        for habit, _ in habitTracker.allHabits["daily"].items():
            streak = habitTracker.calculate_longest_streak(habitTracker.allHabits["daily"][habit])
            print(f"Streak for {habit}: {streak}")
        for habit, _ in habitTracker.allHabits["weekly"].items():
            streak = habitTracker.calculate_longest_streak(habitTracker.allHabits["weekly"][habit])
            print(f"Streak for {habit}: {streak}")

    elif choice1 == "4":
        habitName = input("Choose a habit ")
        streak = habitTracker.calculate_longest_streak(habitName)
        print(f"Longest streak for {habitName}: {streak}")

    elif choice1 == "5":
        break

    else:
        print("Enter 1, 2, 3, 4, 5")
