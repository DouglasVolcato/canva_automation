from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import csv
import time

log_file = 'src/logs/input_log.csv'
exit_program = False
last_action_time = None

def log_mouse_click(x, y, button, pressed):
    global exit_program, last_action_time
    if exit_program:
        return False
    action_time = time.time()
    duration = action_time - last_action_time if last_action_time else 0
    last_action_time = action_time
    if pressed:
        with open(log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([True, button, (x, y), None, duration])  # False for non-time action

def log_key_press(key):
    global exit_program, last_action_time
    action_time = time.time()
    duration = action_time - last_action_time if last_action_time else 0
    last_action_time = action_time
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        pressedKey = ''
        try:
            pressedKey = key.char
        except AttributeError:
            if key == key.esc:
                exit_program = True
                return False
            pressedKey = key
        writer.writerow([False, None, None, pressedKey, duration])  # False for non-time action

with MouseListener(on_click=log_mouse_click) as mouse_listener, \
        KeyboardListener(on_press=log_key_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()

