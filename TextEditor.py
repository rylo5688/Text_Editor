import os
import sys

uIn = raw_input("Would you like to open a file(Y/N) ").upper()

while uIn != "Y" and uIn != "N":
    uIn = raw_input("Would you like to open a file(Y/N) ")

if uIn == "Y":
    uFileName = raw_input("Enter in a file name: ")

    #checking if the file exists
    found = os.path.isfile("./" + uFileName + ".txt")
    while not found: #will loop until the user enters in a valid file
        print "That file doesn't exist!"
        print "If you'd like to exit type \"exit\""
        uFileName = raw_input("Enter in a file name: ")
        if uFileName == "exit":
            sys.exit()
        found = os.path.isfile("./" + uFileName + ".txt")

    #user has entered a real file name
    uFile = open(uFileName + ".txt", "a+")

    exit = False; #bool for the user exit status

    while not exit: #loops until the user types in the exit command 'cmdExit'
        uFile.seek(0, 0) #resets cursor to be at the beginning for the read() function
        content = uFile.read()
        print content
        uWrite = raw_input()
        if uWrite == "cmdExit": #implement with button when GUI is up
            sys.exit() #exits out of the program, maybe ask if they want to save here?
        uFile.write(uWrite + "\n")
    uFile.close()
else: #if they entered 'N' - to be implemented later
    sys.close()
print "We out!"
