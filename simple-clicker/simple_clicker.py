import pyautogui
import time
step = [i for i in range(0, 20000, 150)]
def click():
    time.sleep(0.99)
    pyautogui.click()
def rightclick():
    pyautogui.mouseDown(button='right')
    time.sleep(2)
    pyautogui.mouseUp(button='right')
    pass
def main():
    for i in range(20000):
        click()
        if i in step:
            rightclick()
main()
