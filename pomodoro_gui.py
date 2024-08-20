import tkinter as tk
from tkinter import ttk
from pomodoro_logic import PomodoroLogic
from sound_manager import SoundManager

class PomodoroGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pymodoro Timer")
        self.master.geometry("300x250")

        self.logic = PomodoroLogic()
        self.sound_manager = SoundManager()

        self.label = ttk.Label(master, text=self.logic.get_time_string(), font=("Arial", 24))
        self.label.pack(pady=20)

        self.total_label = ttk.Label(master, text=self.logic.get_total_work_time_string(), font=("Arial", 12))
        self.total_label.pack(pady=10)

        self.button_frame = ttk.Frame(master)
        self.button_frame.pack(pady=10)

        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.toggle_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.reset_main_button = ttk.Button(self.button_frame, text="Reset Timer", command=self.reset_main_timer)
        self.reset_main_button.grid(row=0, column=1, padx=5)

        self.reset_total_button = ttk.Button(self.button_frame, text="Reset Total", command=self.reset_total_work_time)
        self.reset_total_button.grid(row=0, column=2, padx=5)

        self.first_start = True
        self.update_display()

    def toggle_timer(self):
        is_running = self.logic.toggle_running()
        if is_running:
            if self.first_start:
                self.sound_manager.play_start_sound()
                self.first_start = False
            self.start_button.config(text="Pause")
            self.countdown()
        else:
            self.start_button.config(text="Resume")

    def countdown(self):
        if self.logic.is_running:
            state_changed = self.logic.tick()
            if state_changed:
                self.sound_manager.play_sound(self.logic.current_state)
            self.update_display()
            self.master.after(1000, self.countdown)

    def update_display(self):
        self.label.config(text=self.logic.get_time_string())
        self.total_label.config(text=self.logic.get_total_work_time_string())

    def reset_main_timer(self):
        self.logic.reset_main_timer()
        self.start_button.config(text="Start")
        self.first_start = True
        self.update_display()

    def reset_total_work_time(self):
        self.logic.reset_total_work_time()
        self.update_display()