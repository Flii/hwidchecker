import os
import subprocess
import time
import clipboard
import keyboard
import ctypes
import sys

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
ctypes.windll.kernel32.SetConsoleTitleW("HWID Checker")

def logo():

    print ("""
╔╗─╔╗╔╗╔╗╔╗╔══╗╔═══╗╔═══╗╔╗─╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗
║║─║║║║║║║║╚╣╠╝╚╗╔╗║║╔═╗║║║─║║║╔══╝║╔═╗║║║║╔╝║╔══╝║╔═╗║
║╚═╝║║║║║║║─║║──║║║║║║─╚╝║╚═╝║║╚══╗║║─╚╝║╚╝╝─║╚══╗║╚═╝║
║╔═╗║║╚╝╚╝║─║║──║║║║║║─╔╗║╔═╗║║╔══╝║║─╔╗║╔╗║─║╔══╝║╔╗╔╝
║║─║║╚╗╔╗╔╝╔╣╠╗╔╝╚╝║║╚═╝║║║─║║║╚══╗║╚═╝║║║║╚╗║╚══╗║║║╚╗
╚╝─╚╝─╚╝╚╝─╚══╝╚═══╝╚═══╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝╚═══╝╚╝╚═╝
    """)

def main():
    check_hwid()

def check_hwid():
    logo()
    print ("Checking HWID")
    time.sleep(0.3)
    os.system('cls')
    logo()
    print ("Checking HWID.")
    time.sleep(0.3)
    os.system('cls')
    logo()
    print ("Checking HWID..")
    time.sleep(0.3)
    os.system('cls')
    logo()
    print ("Checking HWID...")
    time.sleep(0.3)
    os.system('cls')
    logo()
    print ("Checking HWID....")
    time.sleep(0.3)
    os.system('cls')
    logo()
    print ("Checking HWID.....")
    time.sleep(0.3)
    os.system('cls')
    logo()
    print ("Checking HWID......")
    time.sleep(0.3)
    get_hwid()

def copy2clip(txt):
    clipboard.copy(hwid)

def quit():
    sys.exit()

def get_hwid():
    os.system('cls')
    logo()
    print ("Your HWID is: " + hwid)
    print("Press C To Copy HWID To Clipboard: ")
    if keyboard.read_key() == "C" or "c":
        copy2clip(hwid)
        print(hwid + " Has Been Copied To Your Clipboard")
    time.sleep(0.5)
main()