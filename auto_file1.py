import pyautogui
import time

time.sleep(3)

# Open Chrome via Win+R
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')
time.sleep(3)

# Click on specific Chrome profile
pyautogui.click(646, 481)  # change to your coordinates
time.sleep(3)

# Now continue as normal
pyautogui.hotkey('ctrl', 'l')
time.sleep(3)
pyautogui.write('https://www.google.com', interval=0.1)
pyautogui.press('enter')
time.sleep(5)

# Type the search
pyautogui.write('south africa vs australia cricket score', interval=0.1)
pyautogui.press('enter')
time.sleep(3)

# Click the first link
pyautogui.click(528, 354)  # adjust this too
print("Done!")
