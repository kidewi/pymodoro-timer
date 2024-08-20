from pomodoro_state import PomodoroState

class PomodoroLogic:
    def __init__(self):
        self.work_duration = 25 * 60
        self.short_break_duration = 10 * 60
        self.long_break_duration = 30 * 60
        self.rounds = 0
        self.total_work_time = 0
        self.current_state = PomodoroState.WORK
        self.time_left = self.work_duration
        self.is_running = False

    def tick(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            return False
        elif self.is_running and self.time_left == 0:
            self.switch_state()
            return True
        return False

    def switch_state(self):
        if self.current_state == PomodoroState.WORK:
            self.total_work_time += self.work_duration
            self.rounds += 1
            if self.rounds % 4 == 0:
                self.current_state = PomodoroState.LONG_BREAK
                self.time_left = self.long_break_duration
            else:
                self.current_state = PomodoroState.SHORT_BREAK
                self.time_left = self.short_break_duration
        else:
            self.current_state = PomodoroState.WORK
            self.time_left = self.work_duration

    def get_time_string(self):
        hours, remainder = divmod(self.time_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def get_total_work_time_string(self):
        hours, remainder = divmod(self.total_work_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"Total work time: {hours:02d}:{minutes:02d}:{seconds:02d}"

    def toggle_running(self):
        self.is_running = not self.is_running
        return self.is_running

    def reset_main_timer(self):
        self.is_running = False
        self.current_state = PomodoroState.WORK
        self.time_left = self.work_duration
        self.rounds = 0

    def reset_total_work_time(self):
        self.total_work_time = 0