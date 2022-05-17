import pyautogui
import time


pyautogui.alert("""Welcome to the mass Twitch Chat Banner

For this script to work you press the okay button and you will have FIVE SECONDS to click on the chatbox as a mod to begin the banning
at the end of this script a box will apear saying the script is done <3
click okay to begin timer""")

time.sleep(5)


for line in open("banlist.txt", "r"):
 
    pyautogui.typewrite("/ban " + line)
     
    pyautogui.press("enter")

pyautogui.alert("""The script is done hit okay to terminate program
<3""")

