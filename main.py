import os
import shutil
import prettytable
import time

# Declaring functions

# Function for organizing files inside folders
def insideFolder(path, folder):
    path = path + "/" + folder

    files = findFiles(path)
    typeCount = findType(files, path)
    isWorkDone = creatAndMove(path, typeCount)

    if isWorkDone:
        print("Organizing folder %s is Successful" %folder)
    else:
        print("Something Went Wrong XD")

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
        if (currentFile[:1] == ".") or (currentFile == "main.py") or (currentFile == "README.md"):
            continue
        else:
            filesInFolder.append(currentFile)

    return filesInFolder

# Function to find the types of files and their count
def findType(files, path):
    typesOfExt = {}
    for current in files:
        currentFile = list(current)
        try:
            indexOfHidden = currentFile.index(".")
            currentExt = "".join(currentFile[char] for char in range(indexOfHidden + 1, len(currentFile)))
        except:
            if os.path.isdir(path + "/" + current):
                currentExt = "folder"
            else:
                currentExt = "none"
        try:
            if typesOfExt[currentExt]:
                typesOfExt[currentExt].append(current)
        except:
            typesOfExt[currentExt] = [current]

    return typesOfExt

# Function to create folder and move files
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
    ".jpeg": "JPEG Image Files",
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
    ".ipynb": "Jupiter NoteBook Files",
    ".java": "Java Source Files",
    ".cpp": "C++ Source Files",
    ".c": "C Source Files",
    ".key": "KeyNote Presentations",
    ".iso": "Disk Images",
    ".torrent": "Torrent files"
}
    types = []
    dirNames = []

    for key in filesTypes.keys():
        types.append(key)
    for ext in types:
        if ext == "folder":
            folders = filesTypes["folder"]
            for folder in folders:
                insideFolder(path, folder)
        if ext == "none":
            nones = filesTypes["none"]
            for none in nones:
                makeDIR("Unknown", path)
                shutil.move((path + "/" + none), (path + "/" + "Unknown" + "/" + none))
                
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

# Pretty Table
initial_head = prettytable.PrettyTable()
initial_mid = prettytable.PrettyTable()
organizing = prettytable.PrettyTable()
close = prettytable.PrettyTable()
notFound = prettytable.PrettyTable()

initial_head.field_names = ["SI No", "Function"]
initial_head.add_row(["1", "Organize"])
initial_head.add_row(["2", "Exit"])
initial_head.add_row(["↓", "Enter the Selection"])

organizing.field_names = ["---Organizing---"]
organizing.add_row(["Wait for a moment..."])

close.field_names = ["You chose to exit"]
close.add_row(["Exiting..."])

notFound.field_names = ["Invalid input!"]
notFound.add_row(["Exiting..."])

# Testing 
isOrganize = True

while isOrganize:
    print(initial_head)
    selection = int(input("Input: "))
    if selection == 1:
        print(organizing)
    elif selection == 2:
        print(close)
        isOrganize == False
        break
    else:
        print(notFound)
        isOrganize == False
        break

    path = os.getcwd()

    files = findFiles(path)
    typeCount = findType(files, path)
    isWorkDone = creatAndMove(path, typeCount)

    if isWorkDone:
        initial_mid.field_names = ["Organizing Successful!!"]
        initial_mid.add_row(["Returning to menu in 2 seconds...."])
        print(initial_mid)
        time.sleep(2)
        os.system("cls")
    else:
        initial_mid.field_names = ["Something Went Wrong!!"]
        initial_mid.add_row(["Returning to menu in 2 seconds...."])
        print(initial_mid)
        time.sleep(2)
        os.system("cls")