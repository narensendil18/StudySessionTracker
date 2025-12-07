"""
Study Session Tracker - Helper Functions
Contains all the core functionality for the study tracker.
"""

import csv
import os
from datetime import datetime

# Data file path (relative to project root where you run the program)
DATA_FILE = "data/study_sessions.csv"
CSV_HEADERS = ["date", "course", "minutes", "notes"]


def display_menu():
    """
    Display the main menu options.
    """
    print("-" * 50)
    print("MENU:")
    print("1. Add Study Session")
    print("2. View All Sessions")
    print("3. View Statistics")
    print("4. Exit")
    print("-" * 50)


def add_session():
    """
    Prompt user for session details and return a session dictionary.
    Returns None if user cancels or input is invalid.
    """
    print("\n--- Add New Study Session ---")

    # Get date
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_input = datetime.now().strftime("%Y-%m-%d")
    else:
        # Validate date format
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("✗ Invalid date format. Please use YYYY-MM-DD.")
            return None

    # Get course name
    course = input("Enter course name (e.g., CS 1064): ").strip()
    if not course:
        print("✗ Course name cannot be empty.")
        return None

    # Get minutes
    minutes_input = input("Enter study time in minutes: ").strip()
    try:
        minutes = int(minutes_input)
        if minutes <= 0:
            print("✗ Minutes must be a positive number.")
            return None
    except ValueError:
        print("✗ Invalid input. Please enter a number.")
        return None

    # Get optional notes
    notes = input("Enter notes (optional, press Enter to skip): ").strip()

    # Return session as dictionary
    return {
        "date": date_input,
        "course": course,
        "minutes": minutes,
        "notes": notes,
    }


def view_all_sessions(sessions):
    """
    Display all logged study sessions in a readable format.
    """
    print("\n" + "=" * 50)
    print("ALL STUDY SESSIONS")
    print("=" * 50)

    if not sessions:
        print("No sessions logged yet. Start studying!\n")
        return

    for i, session in enumerate(sessions, 1):
        print(f"\nSession {i}:")
        print(f"  Date: {session['date']}")
        print(f"  Course: {session['course']}")
        print(f"  Time: {session['minutes']} minutes")
        if session.get("notes"):
            print(f"  Notes: {session['notes']}")

    print("\n" + "=" * 50 + "\n")


def display_stats(sessions):
    """
    Calculate and display study statistics.
    """
    print("\n" + "=" * 50)
    print("STUDY STATISTICS")
    print("=" * 50)

    if not sessions:
        print("No data available yet.\n")
        return

    # Calculate total minutes
    total_minutes = sum(int(s["minutes"]) for s in sessions)

    # Calculate per-course totals using dictionary
    course_totals = {}
    for session in sessions:
        course = session["course"]
        minutes = int(session["minutes"])
        course_totals[course] = course_totals.get(course, 0) + minutes

    # Display total time
    hours = total_minutes // 60
    mins = total_minutes % 60
    print(f"\nTotal Study Time: {total_minutes} minutes ({hours}h {mins}m)")

    # Display per-course breakdown
    print("\nTime per Course:")
    for course, minutes in sorted(course_totals.items()):
        h = minutes // 60
        m = minutes % 60
        print(f"  {course}: {minutes} minutes ({h}h {m}m)")

    print("\n" + "=" * 50 + "\n")


def load_data():
    """
    Load existing study sessions from CSV file.
    Returns list of session dictionaries.
    """
    sessions = []

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Check if file exists
    if not os.path.exists(DATA_FILE):
        # Create empty file with headers
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
        return sessions

    # Read existing data
    try:
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sessions.append(row)
    except Exception as e:
        print(f"Warning: Could not load data file: {e}")

    return sessions


def save_data(sessions):
    """
    Save all study sessions to CSV file.
    """
    try:
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(sessions)
    except Exception as e:
        print(f"Error: Could not save data: {e}")