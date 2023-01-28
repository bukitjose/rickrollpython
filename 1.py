import getpass
import pyautogui
import sys
import time

username = getpass.getuser()
print("Hello, " + username + "!")

# Open Notepad
pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('notepad')
pyautogui.hotkey('enter')

# wait for 2 sec to focus on notepad
time.sleep(2)

# Type the word "username:" in Notepad
pyautogui.typewrite("Hi! i see you ")

# Type the actual username in Notepad
pyautogui.typewrite(username)

sys.exit()
