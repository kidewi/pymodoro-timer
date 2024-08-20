Pymodoro Timer
<p align="center">
  <img src="/img/main.png" alt="Pymodoro Timer Main Interface">
</p>
Overview
Pymodoro Timer is a customizable Pomodoro Technique timer application built with Python. It helps you boost productivity by breaking your work into focused intervals, traditionally 25 minutes in length, separated by short breaks.
Features

🍅 Customizable work, short break, and long break durations
🔔 Sound notifications for interval changes
📊 Session logging and total work time tracking
🔄 Ability to reset current timer, total time, or clear logged sessions
💾 Persistent storage of work sessions in JSON format
🖥️ User-friendly GUI built with tkinter

Installation
Prerequisites

Python 3.7 or higher
pip (Python package installer)

Steps

Clone the repository:
Copygit clone https://github.com/kidewi/pymodoro-timer.git
cd pymodoro-timer

Install the required dependencies:
Copypip install -r requirements.txt

Run the application:
Copypython main.py


Usage

Click "Start" to begin the Pomodoro timer.
Work until the timer sounds, then take a break.
Use the "Reset Current" button to reset the timer for the current mode.
"Reset All" will reset the entire cycle back to the first work session.
"Reset Total" clears the accumulated work time for the current run.
"Load Total" retrieves previously logged work sessions.
"Clear Logged" erases all stored work session data.

Creating an Executable
To create a standalone executable:

Install PyInstaller:
Copypip install pyinstaller

Run PyInstaller:
Copypyinstaller pomodoro.spec

Find the executable in the dist folder.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

The Pomodoro Technique® and Pomodoro™ are trademarks of Francesco Cirillo.
Sound effects obtained from ZapSplat.

Contact
If you have any questions, feel free to reach out to Your Name.

Happy focusing with Pymodoro Timer! 🍅✨