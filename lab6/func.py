import pyautogui
from pynput.keyboard import Key
from main import *

word = ""
text = ""
text_right = ""
count = 0


def on_press(key):
    pass


def on_release(key):
    global text_right, text
    symbol = "{0}".format(key)[1]
    text_right += symbol
    text += symbol
    if kmp(word, text_right) != -1:
        global count
        count += 1
        text_right = text_right[len(text_right) - 2:-1]
    cls()
    print(word)
    print(count)
    print(text, end="")
    if key == Key.esc:
        # Stop listener
        return False


def cls():
    # print(pyautogui.position())
    pyautogui.click(x=68, y=653)
    # pyautogui.hotkey("command", ";")
