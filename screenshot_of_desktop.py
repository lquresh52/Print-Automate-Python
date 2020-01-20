import pyautogui
import time


x=1
while x<4:
    pyautogui.screenshot('D:\Desktop\Codes\Python\Print_Automate_Chrome_Page\img'+str(x)+'.png')
    x+=1
    time.sleep(2)