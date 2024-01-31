# Habit_Tracking_App
This Python script is a simple Habit Tracker that allows users to add, remove, and mark habits on a daily or weekly basis. The program provides functionalities such as listing all currently tracked habits, listing habits with the same periodicity, calculating the longest-running streak for all habits, and calculating the longest-running streak for a specific habit.

Usage
To use the Habit Tracker, run the script and follow the on-screen prompts. You can perform the following actions:

Add a habit: Add a new habit to the daily or weekly list.

Remove a habit: Remove an existing habit from the daily or weekly list.

Mark a habit: Mark a habit as completed for the current date.

Exit: Save the habit data to the "habit_data.json" file and exit the program.

After exiting, you can access additional functionalities:

List of all currently tracked habits: Display a list of all habits, categorized as daily or weekly, along with their completion dates.

List of all habits with the same periodicity: Display a list of habits with their completion dates, grouped by their periodicity (daily or weekly).

Longest running streak of all habits: Calculate and display the longest running streak for each habit, considering daily and weekly habits.

Longest running streak of a given habit: Choose a specific habit, and the program will calculate and display its longest running streak.

Exit: Exit the program.

Data Storage
The habit data is stored in a JSON file named "habit_data.json." Upon initialization, the program loads existing data from this file and saves the updated data when exiting.

Requirements
Python 3.x

Note
Make sure to input valid choices as instructed. For date formatting, the script uses the "dd-mm-yyyy" format.
