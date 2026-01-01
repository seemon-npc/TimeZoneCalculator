# Time Zone Calculator

A simple and elegant GUI application for converting time between different time zones. Built with Python's tkinter library, featuring a modern dark-themed interface.

## Features

- ✨ Clean and modern dark-themed user interface
- 🌍 Support for multiple time zones including:
  - India (IST)
  - UTC
  - USA (EST and PST)
  - UK (BST)
  - Japan (JST)
  - Australia (AEST)
- ⏰ Easy time conversion between any two time zones
- 📅 Automatic date handling with conversion results
- 🎯 Simple and intuitive user experience

## Requirements

- Python 3.9 or higher (for `zoneinfo` support)
- tkinter (usually included with Python installations)
- No additional packages required (uses standard library only)

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.9+ installed
3. No additional installation steps required!

## Usage

1. Run the application:
   ```bash
   python timezone.py
   ```

2. Enter a time in HH:MM format (24-hour format, e.g., `14:30`)

3. Select the source time zone from the "From Time Zone" dropdown

4. Select the target time zone from the "To Time Zone" dropdown

5. Click the "Convert Time" button

6. The converted time will be displayed with the date below the button

## Supported Time Zones

- **India (IST)** - Asia/Kolkata
- **UTC** - Coordinated Universal Time
- **USA (EST)** - America/New_York
- **USA (PST)** - America/Los_Angeles
- **UK (BST)** - Europe/London
- **Japan (JST)** - Asia/Tokyo
- **Australia (AEST)** - Australia/Sydney

## How It Works

The application uses Python's built-in `zoneinfo` module to handle time zone conversions accurately. When you enter a time and select source and destination time zones, the application:

1. Parses your input time
2. Assigns it to the source time zone
3. Converts it to the destination time zone
4. Displays the result with the appropriate date

## Notes

- The application uses 24-hour time format (HH:MM)
- Time conversions automatically account for daylight saving time (DST) when applicable
- The date displayed in results corresponds to the converted time zone

## License

This project is open source and available for personal and educational use.

