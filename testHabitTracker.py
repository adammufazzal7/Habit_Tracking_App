import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
import json
import os
from habitTracker import HabitTracker

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        # Create a temporary habit_data.json file for testing
        self.test_data_filename = "test_habit_data.json"
        self.habit_tracker = HabitTracker()

    def tearDown(self):
        # Remove the temporary habit_data.json file after testing
        if os.path.exists(self.test_data_filename):
            os.remove(self.test_data_filename)

    def test_add_habit(self):
        with patch("builtins.input", side_effect=["daily", "Sleeping"]):
            self.habit_tracker.addHabit("Sleeping", "daily")
        self.assertIn("Sleeping", self.habit_tracker.allHabits["daily"])

    def test_add_existing_habit(self):
        self.habit_tracker.allHabits["daily"]["Sleeping"] = ["2023-01-01"]
        with patch("builtins.input", side_effect=["daily", "Sleeping"]):
            self.habit_tracker.addHabit("Sleeping", "daily")
        self.assertEqual(len(self.habit_tracker.allHabits["daily"]["Sleeping"]), 1)

    def test_remove_habit(self):
        self.habit_tracker.allHabits["daily"]["Sleeping"] = ["2023-01-01"]
        with patch("builtins.input", side_effect=["daily", "Sleeping"]):
            self.habit_tracker.removeHabit("Sleeping", "daily")
        self.assertNotIn("Sleeping", self.habit_tracker.allHabits["daily"])

    def test_remove_nonexistent_habit(self):
        with patch("builtins.input", side_effect=["daily", "Sleeping"]):
            self.habit_tracker.removeHabit("Sleeping", "daily")
        self.assertNotIn("Sleeping", self.habit_tracker.allHabits["daily"])

    def test_mark_habit(self):
        with patch("builtins.input", side_effect=["daily", "Sleeping", "2023-01-01"]):
            self.habit_tracker.markHabit("Sleeping", "2023-01-01", "daily")
        self.assertIn("2023-01-01", self.habit_tracker.allHabits["daily"]["Sleeping"])

    def test_mark_existing_habit(self):
        self.habit_tracker.allHabits["daily"]["Sleeping"] = ["2023-01-01"]
        with patch("builtins.input", side_effect=["daily", "Sleeping", "2023-01-01"]):
            self.habit_tracker.markHabit("Sleeping", "2023-01-01", "daily")
        self.assertEqual(len(self.habit_tracker.allHabits["daily"]["Sleeping"]), 1)

    def test_longest_streak(self):
        self.habit_tracker.allHabits["daily"]["Sleeping"] = ["2023-01-01", "2023-01-02", "2023-01-03"]
        streak = self.habit_tracker.longestStreak("Sleeping")
        self.assertEqual(streak, 3)

    def test_longest_streak_weekly(self):
        self.habit_tracker.allHabits["weekly"]["Swimming"] = ["2023-01-01", "2023-01-08", "2023-01-15"]
        streak = self.habit_tracker.longestStreakWeekly("Swimming")
        self.assertEqual(streak, 3)

    def test_load_habit_data(self):
        # Create a temporary habit_data.json file with test data
        test_data = {"daily": {"Sleeping": ["2023-01-01"]}}
        with open(self.test_data_filename, "w") as json_file:
            json.dump(test_data, json_file)

        # Initialize a new HabitTracker instance to load the test data
        habit_tracker = HabitTracker()
        self.assertEqual(habit_tracker.allHabits, test_data)

if __name__ == "__main__":
    unittest.main()