import os
import shutil

# Declaring functions

# Function for creating a Directory
def makeDIR(name, parentDIR):
    try:
        path = os.path.join(parentDIR, name)
        os.mkdir(path)
    except:
        print("Folder Already Exists, so skipping!")

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

def creatAndMove(path, filesTypes):
    fileExtensions = {
    ".txt": "Text Files",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".xls": "Excel Spreadsheets",
    ".xlsx": "Excel Spreadsheets",
    ".ppt": "PowerPoint Presentations",
    ".pptx": "PowerPoint Presentations",
    ".pdf": "PDF Files",
    ".jpg": "JPEG Image Files",
    ".png": "PNG Image Files",
    ".gif": "GIF Image Files",
    ".mp3": "MP3 Audio Files",
    ".mp4": "MP4 Video Files",
    ".avi": "AVI Video Files",
    ".exe": "Executable Files",
    ".zip": "ZIP Archives",
    ".rar": "RAR Archives",
    ".html": "HTML Files",
    ".css": "CSS Stylesheets",
    ".js": "JavaScript Files",
    ".py": "Python Scripts",
    ".java": "Java Source Files",
    ".cpp": "C++ Source Files",
    ".c": "C Source Files",
}
    types = []
    dirNames = []

    for key in filesTypes.keys():
        types.append(key)
    for ext in types:
        extension = "." + ext
        if extension in fileExtensions.keys():
            dirNames.append(fileExtensions[extension])
    for name in dirNames:
        makeDIR(name, path)
        CurrentExt = list(fileExtensions.keys())[list(fileExtensions.values()).index(name)][1:]
        files = filesTypes[CurrentExt]
        for moveFiles in files:
            shutil.move((path + "/" + moveFiles), (path + "/" + name + "/" + moveFiles))
    return True
# Testing 
path = os.getcwd() + "/TestFolder"

files = findFiles(path)
typeCount = findType(files)

isWorkDone = creatAndMove(path, typeCount)

if isWorkDone:
    print("Organizing Successful!!")
else:
    print("Something Went Wrong XD")