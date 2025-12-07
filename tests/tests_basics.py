"""
Basic Tests for Study Session Tracker
Tests core functionality without requiring user input.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from functions import load_data, save_data

def test_save_and_load():
    """Test that we can save and load data correctly."""
    print("Testing save and load functionality...")
    
    # Create test data
    test_sessions = [
        {'date': '2024-12-01', 'course': 'CS 1064', 'minutes': '60', 'notes': 'Chapter 1'},
        {'date': '2024-12-02', 'course': 'MATH 1226', 'minutes': '90', 'notes': 'Derivatives'},
        {'date': '2024-12-03', 'course': 'CS 1064', 'minutes': '45', 'notes': 'Loops practice'}
    ]
    
    # Save test data
    save_data(test_sessions)
    print("✓ Data saved")
    
    # Load data back
    loaded_sessions = load_data()
    print("✓ Data loaded")
    
    # Verify
    if len(loaded_sessions) == len(test_sessions):
        print(f"✓ Correct number of sessions: {len(loaded_sessions)}")
    else:
        print(f"✗ Error: Expected {len(test_sessions)}, got {len(loaded_sessions)}")
    
    print("\nLoaded sessions:")
    for i, session in enumerate(loaded_sessions, 1):
        print(f"  {i}. {session['date']} - {session['course']} - {session['minutes']} min")
    
    print("\nTest complete!\n")

def test_statistics():
    """Test statistics calculation manually."""
    print("Testing statistics calculation...")
    
    sessions = [
        {'date': '2024-12-01', 'course': 'CS 1064', 'minutes': '60', 'notes': ''},
        {'date': '2024-12-02', 'course': 'MATH 1226', 'minutes': '90', 'notes': ''},
        {'date': '2024-12-03', 'course': 'CS 1064', 'minutes': '45', 'notes': ''}
    ]
    
    # Calculate totals
    total = sum(int(s['minutes']) for s in sessions)
    print(f"Total minutes: {total} (expected: 195)")
    
    # Calculate per course
    course_totals = {}
    for s in sessions:
        course = s['course']
        mins = int(s['minutes'])
        course_totals[course] = course_totals.get(course, 0) + mins
    
    print("Per-course totals:")
    print(f"  CS 1064: {course_totals.get('CS 1064', 0)} (expected: 105)")
    print(f"  MATH 1226: {course_totals.get('MATH 1226', 0)} (expected: 90)")
    
    print("\nTest complete!\n")

if __name__ == "__main__":
    print("=" * 50)
    print("RUNNING BASIC TESTS")
    print("=" * 50)
    print()
    
    test_save_and_load()
    test_statistics()
    
    print("=" * 50)
    print("ALL TESTS COMPLETE")
    print("=" * 50)