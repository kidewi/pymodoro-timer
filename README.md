# Pymodoro Timer

<p align="center">
  <img src="/img/main.png" alt="Pymodoro Timer Main Interface">
</p>

## Overview

Pymodoro Timer is a customizable Pomodoro Technique timer application built with Python. It helps you boost productivity by breaking your work into focused intervals, traditionally 25 minutes in length, separated by short breaks.

## Features

- 🕑 Customizable work, short break, and long break durations
- 🔔 Sound notifications for interval changes
- 📊 Session logging and total work time tracking
- 🔄 Ability to reset current timer, total time, or clear logged sessions
- 💾 (TO-DO) Persistent storage of work sessions in JSON format
- 🖥️ User-friendly GUI built with tkinter

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/kidewi/pymodoro-timer.git
   cd pymodoro-timer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Click "Start" to begin the Pomodoro timer.
2. Work until the timer sounds, then take a break.
3. Use the "Reset Current" button to reset the timer for the current mode.
4. "Reset All" will reset the entire cycle back to the first work session.
5. "Reset Total" clears the accumulated work time for the current run.
6. "Load Total" retrieves previously logged work sessions.
7. "Clear Logged" erases all stored work session data.

## Creating an Executable

To create a standalone executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run PyInstaller:
   ```bash
   pyinstaller pomodoro.spec
   ```

3. Find the executable in the `dist` folder.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- The Pomodoro Technique® and Pomodoro™ are trademarks of Francesco Cirillo.
- Sound effects obtained from [ZapSplat](https://www.zapsplat.com).

## Contact

If you have any questions, feel free to reach out to [Kirk Wilson](kirkdwilson@outlook.com).

---

Happy focusing with Pymodoro Timer!