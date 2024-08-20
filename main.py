import tkinter as tk
from pomodoro_gui import PomodoroGUI

def main():
    root = tk.Tk()
    app = PomodoroGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()