#Python Awesome Python Terminal v0.2 by Cosmic Open Source Projects
#Recreating the python terminal with less than 30 lines of code!
        
import sys

print("AwesomePythonTerminal v0.2")
print("Python " + sys.version)
print('Type "help", "copyright", "credits" or "license" for more information.')

running = True

while running == True:

    command = input(">>> ")
    
    if command == "exit":
        
        running = False
    
    if command == "help":
        
        print("Awesome Python Terminal v0.1.2 by Cosmic Open Source Projects")
        print()
        print("Learn More at https://github.com/ilovecode1/AwesomePythonTerminal")
        print("-----------------------------------------------------------------")
        help()
    
    exec command
    
sys.exit()
