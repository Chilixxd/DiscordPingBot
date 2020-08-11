#PingBot
#Made by Chili
#Version 2.0 (Final Release)
#Date 2020-08-09

from pynput.keyboard import Key, Controller
import os, time, sys
keyboard = Controller()

print("__________.__              __________        __   ")
print("\______   \__| ____    ____\______   \ _____/  |_ ")
print(" |     ___/  |/    \  / ___\|    |  _//  _ \   __\ ")
print(" |    |   |  |   |  \/ /_/  >    |   (  <_> )  |  ")
print(" |____|   |__|___|  /\___  /|______  /\____/|__|  ")
print("                  \//_____/        \/             ")
print("")
print("[+] To begin, python3 PingBot.py -h or --help")

helpmenu = """

Welcome to the help menu of PingBot!

Commands: 

-u = Username

-e = Everyone

-c= Custom word to get spammed
--custom = Custom word to get spammed

Example: python3 PingBot.py -u
...
Enter the username: discord 123
"""

if '--help' in sys.argv:
    print(helpmenu)

if '-h' in sys.argv:
    print(helpmenu)

if '-u' in sys.argv:
    username = input("Enter the username: ")
    pinged1 = int(input("How many pings?: "))

    print("[+] Made by Chili")
    print("")
    print("[+] Script Starting in 5 seconds")
    time.sleep(1)
    print("[+] Script Starting in 4 seconds") 
    time.sleep(1)
    print("[+] Script Starting in 3 seconds")
    time.sleep(1)
    print("[+] Script Starting in 2 seconds")
    time.sleep(1)
    print("[+] Script Starting in 1 second")   

    for x in range(pinged1):
         keyboard.type("@" + username)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)


if '-e' in sys.argv:

    pinged2 = int(input("How many pings?: "))
    e = ("everyone")
    print("[+] Made by Chili")
    print("")
    print("[+] Script Starting in 5 seconds")
    time.sleep(1)
    print("[+] Script Starting in 4 seconds") 
    time.sleep(1)
    print("[+] Script Starting in 3 seconds")
    time.sleep(1)
    print("[+] Script Starting in 2 seconds")
    time.sleep(1)
    print("[+] Script Starting in 1 second")

    for x in range(pinged2):
         keyboard.type("@" + e)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)

if '--custom' in sys.argv: 
   custom = input('Enter the word to get spammed: ')
   pinged3 = int(input('How many times should the word/sentence get spammed?: '))
   
   print("[+] Made by Chili")
   print("")
   print("[+] Script Starting in 5 seconds")
   time.sleep(1)
   print("[+] Script Starting in 4 seconds") 
   time.sleep(1)
   print("[+] Script Starting in 3 seconds")
   time.sleep(1)
   print("[+] Script Starting in 2 seconds")
   time.sleep(1)
   print("[+] Script Starting in 1 second")


   for x in range(pinged3):
       keyboard.type(custom)
       keyboard.press(Key.enter)
       keyboard.release(Key.enter)
       keyboard.press(Key.enter)
       keyboard.release(Key.enter)

if '-c' in sys.argv: 
   custom = input('Enter the word to get spammed: ')
   pinged3 = int(input('How many times should the word/sentence get spammed?: '))
   
   print("[+] Made by Chili")
   print("")
   print("[+] Script Starting in 5 seconds")
   time.sleep(1)
   print("[+] Script Starting in 4 seconds") 
   time.sleep(1)
   print("[+] Script Starting in 3 seconds")
   time.sleep(1)
   print("[+] Script Starting in 2 seconds")
   time.sleep(1)
   print("[+] Script Starting in 1 second")


   for x in range(pinged3):
       keyboard.type(custom)
       keyboard.press(Key.enter)
       keyboard.release(Key.enter)
       keyboard.press(Key.enter)
       keyboard.release(Key.enter)
