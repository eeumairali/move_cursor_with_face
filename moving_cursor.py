import pyautogui
import keyboard
step_size = 20

while True:
    if keyboard.is_pressed('q'):
        break
    if keyboard.is_pressed('up'):
        pyautogui.move(0, -step_size)
    if keyboard.is_pressed('down'):
        pyautogui.move(0, step_size)
    if keyboard.is_pressed('left'):
        pyautogui.move(-step_size, 0)
    if keyboard.is_pressed('right'):
        pyautogui.move(step_size, 0)
    if keyboard.is_pressed('space'):
        pyautogui.click()
    pyautogui.sleep(0.0001)