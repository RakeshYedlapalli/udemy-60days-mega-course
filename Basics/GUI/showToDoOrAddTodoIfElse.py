import time
from fynctins import listUsers, readFile, readFromFile, writeFile


userPrompt = []




while True:
    inputPrompt = input("Do you want to add or see, Please enter your option either 'add' or 'see' or delete or edit: ")
    if inputPrompt.startswith('add'):
        inputValue = inputPrompt[4:]+"\n"
        userPrompt = readFile()
        userPrompt.append(inputValue)
        writeFile(userPrompt) 
    elif inputPrompt.startswith('see'):
            readFromFile()
            listUsers(userPrompt)
    elif inputPrompt.startswith('complete'):
            # number = input("Enter the Index of the name to be removed: ")
            castedValue = int(inputPrompt[9:])
            readFromFile()
            print("I will be removing the name :", userPrompt[castedValue])
            userPrompt = readFile() 
            del userPrompt[castedValue]
            writeFile(userPrompt)
            print("removed the element successfully, please enter see to view the list")

    elif inputPrompt.startswith('edit'):
          readFromFile()
            # number = input("Enter the Index of the name to be edited: ")
        #     if(inputPrompt[5:].isdigit()):
          try:
            castedValue = int(inputPrompt[5:])
            newTodo = input("Enter the new Todo to be replaced: ")+"\n"
            userPrompt[castedValue] = newTodo
            writeFile(userPrompt)
            print("Replaced the todo successfully")
          except ValueError:
            print("Please enter only the digits", ValueError)
    elif inputPrompt.startswith('deleteAll'):
        userPrompt.clear()
        writeFile(userPrompt) 
    elif inputPrompt.startswith('date'):
         print(time.strftime("%Y-%m-%d"))
            
#     else:
        #     print("Enter only the digits to be edited")
    elif inputPrompt.startswith('exit'):
            break
    else:
           print("You have selected wrong option")