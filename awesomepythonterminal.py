#Python AwesomePythonTerminal v0.1 by Cosmic Open Source Projects
#Recreating the python terminal with less than 30 lines of code!
        
import sys
import os

print("AwesomePythonTerminal v0.1")
print('Type "help", "copyright", "credits" or "license" for more information.')
print(sys.version)

running = True

while running == True:

    command = input(">>> ")
        
    if command == "exit":
    
        sys.exit()
        
    exec command
