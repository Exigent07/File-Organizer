import os
import shutil

def organizeFolder(folderPath):
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
            if (currentFile[:1] == ".") or (currentFile == "main.py") or (currentFile == "README.md") or (currentFile == "app.py"):
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
                currentExt = "." + "".join(currentFile[char] for char in range(indexOfHidden + 1, len(currentFile)))
                # print("FindType: ", currentExt)
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
        ".docx": "WordX Documents",
        ".xls": "Excel Spreadsheets",
        ".xlsx": "Excel Spreadsheets",
        ".ppt": "PowerPoint Presentations",
        ".pptx": "PowerPoint TX Presentations",
        ".pdf": "PDF Files",
        ".jpg": "JPG Image Files",
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
        ".torrent": "Torrent files",
        "unknown": "Unknown"
    }
        types = []
        dirNames = []

        for key in filesTypes.keys():
            types.append(key)
        for ext in types:
            if ext == "folder":
                folders = filesTypes["folder"]
                # print("Folders", folders)
                for folder in folders:
                    # print(folder)
                    if folder in fileExtensions.values():
                        # print("Hit the folder loop")
                        continue
                    insideFolder(path, folder)
            elif ext == "none":
                nones = filesTypes["none"]
                for none in nones:
                    makeDIR("Unknown", path)
                    shutil.move((path + "/" + none), (path + "/" + "Unknown" + "/" + none))
            else:
                extension = ext
                # print(extension)
                if extension in fileExtensions.keys():
                    dirNames.append(fileExtensions[extension])
                    print(fileExtensions[extension])
        for name in dirNames:
            # print("Name:", name)
            makeDIR(name, path)
            CurrentExt = "." + list(fileExtensions.keys())[list(fileExtensions.values()).index(name)][1:]
            # print(CurrentExt)
            files = filesTypes[CurrentExt]
            for moveFiles in files:
                shutil.move((path + "/" + moveFiles), (path + "/" + name + "/" + moveFiles))
        return True

    path = folderPath

    files = findFiles(path)
    typeCount = findType(files, path)
    isWorkDone = creatAndMove(path, typeCount)

    return isWorkDone