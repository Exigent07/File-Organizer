import os

path = os.getcwd()
filesInFolder = []

for item in (os.listdir(path + "/TestFolder")):
    currentFile = item
    if (currentFile[:1] == "."):
        continue
    else:
        filesInFolder.append(currentFile)

print(filesInFolder)