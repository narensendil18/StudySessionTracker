# Study Session Tracker

A simple command-line Python application for college students to track and analyze their study sessions across multiple courses.

## Project Overview

The Study Session Tracker helps students monitor how they allocate their study time. By logging each study session with details like date, course, and duration, students can gain insights into their study habits and identify which courses need more attention.

## Video Demonstration

https://www.youtube.com/watch?v=2dkn4ZPlQ3Q

## Features

- **Add Study Sessions**: Log study sessions with date, course name, duration (in minutes), and optional notes
- **View All Sessions**: Display a complete list of all logged study sessions
- **View Statistics**: Calculate and display:
  - Total study time across all courses
  - Study time breakdown per course
  - Time formatted in hours and minutes for easy reading
- **Persistent Storage**: All data saved to CSV file and loaded automatically on startup

## Technologies Used

- **Python 3.x** - Core programming language
- **csv module** - For reading and writing session data
- **datetime module** - For date validation and formatting
- **os module** - For file system operations

## Installation and Setup

### Prerequisites

- Python on your system
- Terminal/Command Prompt access

**Directory structure:**
   
   study-session-tracker/
   ├── code/
   │   ├── study_tracker.py
   │   └── functions.py
   ├── data/
   │   └── (study_sessions.csv will be created here)
   ├── tests/
   │   ├── test_basic.py
   │   └── test_cases.txt
   ├── docs/
   ├── report/
   └── README.md


## How to Run

### Running the Main Program

1. In terminal: 

python code/study_tracker.py


2. Follow the on-screen menu:
   ```
   MENU:
   1. Add Study Session
   2. View All Sessions
   3. View Statistics
   4. Exit
   ```

### Running Tests

To verify the program works correctly:

python tests/test_basic.py

This will test data saving/loading and statistics calculations.

## Usage Examples

### Adding a Study Session

```
Enter your choice (1-4): 1

--- Add New Study Session ---
Enter date (YYYY-MM-DD) or press Enter for today: 2024-12-06
Enter course name (e.g., CS 2104): CS 2104
Enter study time in minutes: 90
Enter notes (optional, press Enter to skip): Worked on loops and functions

✓ Session added successfully!
```

### Viewing Statistics

```
Enter your choice (1-4): 3

==================================================
STUDY STATISTICS
==================================================

Total Study Time: 285 minutes (4h 45m)

Time per Course:
  CS 2104: 135 minutes (2h 15m)
  ENGL 1106: 60 minutes (1h 0m)
  MATH 1226: 90 minutes (1h 30m)

==================================================
```

## File Descriptions

- **code/study_tracker.py** - Main program entry point with menu loop
- **code/functions.py** - Helper functions for all core functionality
- **data/study_sessions.csv** - CSV file storing all study session data
- **tests/test_basic.py** - Automated tests for save/load and statistics
- **tests/test_cases.txt** - Manual test case documentation
- **README.md** - This file

## Project Structure

```
├── code/           # Source code files
├── data/           # Data storage (CSV files)
├── tests/          # Test files
├── docs/           # Documentation and screenshots
├── report/         # Project report
└── README.md       # Project documentation
```

## Author

Naren Sendil Kumar
CS2104 Personal Project

## Contribution Summary

This project was completed for the CS 2104 Personal Programming Project. All design decisions, implementation, and testing were performed by the author with assistance from:
- TA office hours for requirement verification
- Python documentation for syntax reference
- Limited LLM usage for debugging and test case generation

## Future Enhancements

- Filter sessions by specific course
- Display most recent N sessions
- Track consecutive study days


