userPrompt = []


def listUsers(userPrompt):
    value = 0
    for indexValue , item  in enumerate(userPrompt):
             indexValue+=1
             print(f"{indexValue}-{item.strip()}")

def readFromFile():
         global userPrompt
         file = open('textFile.txt', 'r')
         userPrompt = file.readlines()
         file.close()
         userPrompt.append("Added")

while True:
    inputPrompt = input("Do you want to add or see, Please enter your option either 'add' or 'see' or delete or edit: ")

    match inputPrompt:

        case 'add':
            inputValue = input("Enter Todo: ")+ "\n"
            file = open('textFile.txt', 'r')
            userPrompt = file.readlines()
            file.close()
            userPrompt.append(inputValue)
            file = open('textFile.txt', 'w')
            file.writelines(userPrompt)
            file.close()
        case 'see':
              readFromFile()
              listUsers(userPrompt)
        case 'complete':
            number = input("Enter the Index of the name to be removed: ")
            castedValue = int(number)
            readFromFile()
            print("I will be removing the name :", userPrompt[castedValue])
            file = open('textFile.txt', 'r')
            userPrompt = file.readlines()
            file.close()
            del userPrompt[castedValue]
            file = open('textFile.txt', 'w')
            file.writelines(userPrompt)
            file.close()
            print("removed the element successfully, please enter see to view the list")

        case 'edit':
            readFromFile()
            number = input("Enter the Index of the name to be edited: ")
            castedValue = int(number)
            newTodo = input("Enter the new Todo to be replaced: ")+"\n"
            userPrompt[castedValue] = newTodo
            file = open('textFile.txt', 'w')
            file.writelines(userPrompt)
            file.close()
            print("Replaced the todo successfully")

        case 'exit':
            break