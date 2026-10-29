import pyautogui
import keyboard
import time

clicking = False
running = True

clicks_per_second = 20
delay = 1 / clicks_per_second

pyautogui.PAUSE = 0


def toggle_clicking():
    global clicking
    clicking = not clicking
    print("Clicking:", clicking)


def stop_program():
    global running
    running = False
    print("Exiting...")


keyboard.add_hotkey("f6", toggle_clicking)
keyboard.add_hotkey("esc", stop_program)

print("Autoclicker ready.")
print("F6 = start/stop")
print("ESC = quit")

while running:
    if clicking:
        pyautogui.click()
        time.sleep(delay)
    else:
        time.sleep(0.01)
