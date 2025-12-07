"""
Study Session Tracker - Main Program
Author: Naren Sendil Kumar

This is the main entry point for the Study Session Tracker application.
It provides a command-line interface for students to log and analyze their study sessions.
"""

import sys
from functions import (
    display_menu,
    add_session,
    view_all_sessions,
    display_stats,
    load_data,
    save_data
)


def main():
    print("=" * 50)
    print("Welcome to Study Session Tracker!")
    print("=" * 50)
    print()

    # Load existing data at startup
    sessions = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Add a new study session
            session = add_session()
            if session:
                sessions.append(session)
                save_data(sessions)
                print("\n✓ Session added successfully!\n")

        elif choice == "2":
            # View all logged sessions
            view_all_sessions(sessions)

        elif choice == "3":
            # Display statistics
            display_stats(sessions)

        elif choice == "4":
            # Exit the program
            print("\nThank you for using Study Session Tracker!")
            print("Keep up the good work!\n")
            sys.exit(0)

        else:
            print("\n Invalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
