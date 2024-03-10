contents = ["FILE1", "FILE2", "FILE3","FILE4"]

fileNames = ["file.txt", "file1.txt", "file2.txt", "file3.txt"]

for fileName, content in zip(fileNames,contents):
    with open(f"files/{fileName}", 'w') as file:
        # file = open(fileName, 'r')
        file.write(content)
        file.close()
