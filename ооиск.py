import pyautogui
import time
import keyboard
g=input('Что нужно?')
if g == 'поиск':
    b=input('ЧЕГО ИСКАть БУдем?')
    pyautogui.moveTo(200,1080)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(200,70)
    pyautogui.click()
    keyboard.write(b)
    pyautogui.prees('enter')
if g == 'текст':
     
     b=input('писать будем?')
     pyautogui.moveTo(100,1080)
     pyautogui.click()
     pyautogui.moveTo(100,470)
     pyautogui.click()
     pyautogui.moveTo(250,350)
     pyautogui.doubleClick()
     pyautogui.moveTo(350,350)
     keyboard.write(b)
if g == 'выход':
    exit()

