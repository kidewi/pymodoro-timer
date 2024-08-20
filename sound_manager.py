import pygame
from pomodoro_state import PomodoroState

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.work_sound = pygame.mixer.Sound("work_chime.wav")
        self.short_break_sound = pygame.mixer.Sound("short_break_chime.wav")
        self.long_break_sound = pygame.mixer.Sound("long_break_chime.wav")
        self.start_sound = pygame.mixer.Sound("start_chime.wav")

    def play_sound(self, state):
        if state == PomodoroState.WORK:
            self.work_sound.play()
        elif state == PomodoroState.SHORT_BREAK:
            self.short_break_sound.play()
        elif state == PomodoroState.LONG_BREAK:
            self.long_break_sound.play()

    def play_start_sound(self):
        self.start_sound.play()