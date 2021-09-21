import pyautogui as py
import webbrowser as web
import time

# message
message = input("what message do you want to spam?\n")

#how many times
repeats = int(input("How many times do you want to spam this message?\n "))

#delay
delay = int(input("How many ms do you wanna wait between each message? \n"))

ready = input("Press enter when you are ready!\n ")

#When you are ready
print("You have five seconds to be ready for spam!\n ")

#five-second time
time.sleep(5)

#Logic of the spammer
for i in range (0, repeats):
    if message != "":
        py.typewrite(message)
        py.press("enter")
        time.sleep(delay/1000)
        
print("Done")
