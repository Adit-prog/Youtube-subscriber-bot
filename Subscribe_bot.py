
import socket
import pyautogui 
import time 
import subprocess
from _thread import *

class SubBot:
    print(".     ███▄ ▄███▓ ▄▄▄        ▄████  ██▓ ▄████▄   ██▓ ▄▄▄       ███▄    █ ")
    print(",    ▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓██▒▒██▀ ▀█  ▓██▒▒████▄     ██ ▀█   █ ")
    print(".    ▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒██▒▒▓█    ▄ ▒██▒▒██  ▀█▄  ▓██  ▀█ ██▒")
    print(".    ▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓░██░▒▓▓▄ ▄██▒░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒")
    print(".    ▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░██░▒ ▓███▀ ░░██░ ▓█   ▓██▒▒██░   ▓██░")
    print(".    ░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░▓  ░ ░▒ ▒  ░░▓   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
    print(".                   Program written by Magician")
    print(".  You can use it for subscribe your youtube channel or modified it for other web apps\n")

    # javascript code for click on subscribe and bell button
    subButton = 'var SubForLogin = document.getElementsByClassName("style-scope ytd-subscribe-button-renderer");'
    subButtonClick = "SubForLogin[1].click();"
    bellButton = 'var Bell = document.getElementsByClassName("style-scope ytd-toggle-button-renderer");'
    bellButtonClick = "Bell[1].click();"    

    # Type here your channel url:
    url = input("Enter your channel link = ")
    
    listOfBrowser = ['start chrome '+url,'start firefox '+url]

    listOfCommand = ['j','i']

    waitTime = 1
    flag = True
    count = 0

    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def enter(self,val):
        time.sleep(self.waitTime)
        pyautogui.press('enter')
      
    def main(self):

        while self.flag:
            
            time.sleep(self.waitTime+4)
            
            if self.is_connected() == True:
                for i in self.listOfBrowser:
                    start_new_thread(self.enter,(1,))
                    process = subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    process.communicate()

                    if process.returncode == 1:
                        self.count = self.count + 1
                        if self.count == len(self.listOfBrowser):
                            self.flag = False;
                        continue

                    time.sleep(self.waitTime+4)
                    pyautogui.hotkey('ctrl','shift',self.listOfCommand[self.listOfBrowser.index(i)])

                    time.sleep(self.waitTime+2)
                    pyautogui.typewrite(self.subButton)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                    pyautogui.typewrite(self.subButtonClick)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                    pyautogui.typewrite(self.bellButton)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                    pyautogui.typewrite(self.bellButtonClick)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                  
                    pyautogui.hotkey('alt','f4')
                  
                    pyautogui.press('enter')

                    self.flag = False;
                    break
            else:
                print("Please Connect to Internet")

subBot = SubBot()
subBot.main()

#Enjoy the program!

