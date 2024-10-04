import pandas as pd
import pyautogui
import time
import csv
import ast
import os


def execute_csv_command(csv_path: str):
    with open(csv_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            is_mouse_click, mouse_button, mouse_coord, key_pressed, time_passed = row
            time.sleep(float(time_passed))
            if is_mouse_click == 'True':
                x, y = ast.literal_eval(mouse_coord)
                mouse_button = str.replace(mouse_button, 'Button.', '')
                if (mouse_button == 'left'):
                    pyautogui.click(x, y)
                else:
                    pyautogui.rightClick()
            else:
                pyautogui.press(str.replace(key_pressed, 'Key.', ''))


def get_file(content_to_write: str):
    time.sleep(2)
    execute_csv_command('csv_commands/click_name_field.csv')
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(content_to_write)

    time.sleep(2)
    execute_csv_command('csv_commands/download.csv')
    time.sleep(7)

def rename_last_downloaded_file(name: str):
    folder = os.path.join(os.path.expanduser("~"), "Downloads")
    files = []

    if os.path.exists(folder):
        files = [
            (os.path.join(folder, f), os.path.getmtime(os.path.join(folder, f)))
            for f in os.listdir(folder)
        ]
        files.sort(key=lambda f: f[1])
        files = [[f[0], f[1]] for f in files]

    if len(files) > 0:
        last_modified_file = files[-1]
        last_modified_file_path = last_modified_file[0]
        last_modified_file_name = last_modified_file[0].split("/")[-1]
        last_modified_file_extension = last_modified_file_name.split(".")[-1]
        os.rename(last_modified_file_path, os.path.join(folder, name + "." + last_modified_file_extension))

exel_with_names = pd.read_excel('data.xlsx')

execute_csv_command('csv_commands/open_browser.csv')
for index, row in exel_with_names.iterrows():
    content_to_write = row['name']
    get_file(content_to_write)
    rename_last_downloaded_file(content_to_write)
execute_csv_command('csv_commands/open_browser.csv')