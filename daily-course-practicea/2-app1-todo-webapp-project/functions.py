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

def readFile():
        file = open('textFile.txt', 'r')
        userPrompt = file.readlines()
        file.close()
        return userPrompt


def writeFile(userPrompt):
        file = open('textFile.txt', 'w')
        file.writelines(userPrompt)
        file.close()