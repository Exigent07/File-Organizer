import os

# Declaring functions

# Function for creating a Directory
def makeDIR(name, parentDIR):
    path = os.path.join(parentDIR, name)
    os.mkdir(path)

# Function for finding Files
def findFiles(path):
    filesInFolder = []

    for item in (os.listdir(path)):
        currentFile = item
        if (currentFile[:1] == "."):
            continue
        else:
            filesInFolder.append(currentFile)

    return filesInFolder

# Function to find the types of files and their count
def findType(files):
    typesOfExt = {}
    for current in files:
        currentFile = list(current)
        indexOfHidden = currentFile.index(".")
        currentExt = "".join(currentFile[char] for char in range(indexOfHidden + 1, len(currentFile)))
        try:
            if typesOfExt[currentExt]:
                typesOfExt[currentExt].append(current)
        except:
            typesOfExt[currentExt] = [current]

    return typesOfExt

# Testing 
path = os.getcwd() + "/TestFolder"

files = findFiles(path)
typeCount = findType(files)

print("Files:", typeCount)

# makeDIR("Test", path)