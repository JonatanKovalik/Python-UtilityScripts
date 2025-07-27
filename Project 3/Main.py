#This code is base 10 to 2 and 2 to 10!!!
#Created by Jonatan Kovalilk!!
#05/01/2025
# ---------------------------------------------------------
import time

def functionquit():
    quest3 = str(input("Do you want to continue or to quit from the program??"))
    if quest3 == "Yes" or quest3 == "yes" or quest3 == "continue" or quest3 == "Continue":
        function()
    elif quest3 == "No" or quest3 == "no" or quest3 == "quit" or quest3 == "Quit":
        print("Thank you for using my program code in python!")
        time.sleep(1.5)
        print("Good bye and good day! :)")
        time.sleep(1)
        exit()

def function():
    quest1 = str(input("What are the base you want to transform 2 to 10 or 10 to 2??")).strip()
    if quest1 == "2 to 10" or quest1 == "2-10" or quest1 == "2 - 10" or quest1 == "2 10":
        quest2 = input("Give me the number base 2").strip()
        try:
            decnum = int(quest2, 2)
            print(f"The decimal value of {quest2} is {decnum}")
            functionquit()
        except ValueError:
            print("Invalid binary number! Please try again.")
            function()

    elif quest1 == "10 to 2" or quest1 == "10-2" or quest1 == "10 - 2" or quest1 == "10 2":
        try:
            quest2 = int(input("Give me the number base 10").strip())
            binnum = bin(quest2)[2:]
            print(f"The binary value of {quest2} is {binnum}")
            functionquit()
        except ValueError:
            print("Invalid decimal number! Please try again.")
            function()
    else:
        print("Invalid option! Please choose '2 to 10' or '10 to 2'.")
        function()

Doyouwantostartascript = str(input("Do you want start this script?")).strip()
if Doyouwantostartascript == "Yes" or Doyouwantostartascript == "yes":
    function()
elif Doyouwantostartascript == "No" or Doyouwantostartascript == "no":
    print("Ok good luck!!")
    exit("Player doesn't want to start the script!")
else:
    exit("Player doesn't want to start the script!")
