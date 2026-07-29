import webbrowser
import pyautogui
import time

query = input("Enter the search query: ")
time.sleep(3)  
webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
time.sleep(9)
pyautogui.click(572,122)
time.sleep(3)
pyautogui.write(query,interval=0.1)
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(519,280)
