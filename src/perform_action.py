import pyautogui
import time
import csv
import ast

with open('src/logs/input_log.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        is_mouse_click, mouse_button, mouse_coord, key_pressed, time_passed = row
        time.sleep(float(time_passed))
        if is_mouse_click == 'True':
            x, y = ast.literal_eval(mouse_coord)
            mouse_button = str.replace(mouse_button,'Button.','')
            if(mouse_button == 'left'):
                pyautogui.click(x, y)
            else:
                pyautogui.rightClick()
        else:
            pyautogui.press(str.replace(key_pressed,'Key.',''))
