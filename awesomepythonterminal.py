#Python Awesome Python Terminal v0.1 by Cosmic Open Source Projects
#Recreating the python terminal with less than 30 lines of code!
        
import sys

print("AwesomePythonTerminal v0.1")
print(sys.version)
print('Type "help", "copyright", "credits" or "license" for more information.')

running = True

while running == True:

    command = input(">>> ")
        
    if command == "exit":
        
        running = False
        
    exec command
    
sys.exit()
