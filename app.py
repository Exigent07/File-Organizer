import sys
import os
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QFileDialog
from PyQt6 import QtWidgets
from time import sleep
from main import organizeFolder

class MainWindow(QMainWindow):
    def __init__(self):
        path = "C:/Users/aravi/Downloads/folder.png"
        super().__init__()
        self.setStyleSheet("background-color: #ffa07a;")
        greet = QLabel("Welcome to File Organizer")
        greet.setStyleSheet("color: #2f4f4f; font-size: 22px; text-align: center; font-weight: bold;") 

        self.organize = QPushButton("Organize", self)
        self.organize.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
        self.organize.setCheckable(True)
        self.organize.setFixedSize(110, 40)
        self.organize.pressed.connect(self.organize_pressed)
        self.organize.released.connect(self.organize_released)
        self.organize.clicked.connect(self.organizing)

        self.selectBtn = QPushButton("Browse")
        self.selectBtn.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
        self.selectBtn.setCheckable(True)
        self.selectBtn.setFixedSize(70, 20)
        self.selectBtn.pressed.connect(self.browse_pressed)
        self.selectBtn.released.connect(self.browse_released)
        self.selectBtn.clicked.connect(self.selectDIR)

        self.inputBox = QLineEdit()
        self.inputBox.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

        self.fileOrganizer = QLabel(self)
        pix = QPixmap(path)
        resized =  pix.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.fileOrganizer.setPixmap(QPixmap(resized))
        self.fileOrganizer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.exit = QPushButton("Exit", self)
        self.exit.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
        self.exit.setCheckable(True)
        self.exit.setFixedSize(110, 40)
        self.exit.pressed.connect(self.exit_pressed)
        self.exit.released.connect(self.exit_released)
        self.exit.clicked.connect(self.quit)

        layout = QVBoxLayout()
        layout.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fileOrganizer, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Folder: "), alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.inputBox, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.selectBtn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.organize, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.exit, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setFixedSize(500, 500)

    def browse_pressed(self):
        self.selectBtn.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def browse_released(self):
        self.selectBtn.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def organize_pressed(self):
        self.organize.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def organize_released(self):
        self.organize.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def exit_pressed(self):
        self.exit.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def exit_released(self):
        self.exit.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def selectDIR(self):
        dirName = QFileDialog.getExistingDirectory(self, "Select a Folder")
        if dirName:
            path = str(dirName)
            self.inputBox.setText(str(path))
            self.folder = str(path)
            print(path)

    def organizing(self):
        folder = self.inputBox.text()
        print(folder)
        if folder == "":
            print("Enter a Folder Path")
        else:
            organizeFolder(folder)    
            widget.setCurrentIndex(2)
            print("Organized")

    def quit(self):
        widget.setCurrentIndex(1)
        QTimer.singleShot(1000, self.exit_application)

    def exit_application(self):
        print("Exited Successfully!")
        sys.exit()

class QuitWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        path = "C:/Users/aravi/Downloads/folder.png"
        self.setStyleSheet("background-color: #ffa07a;")
        self.setWindowTitle("File Organizer")
        self.setWindowIcon(QIcon(path))

        greet = QLabel("Thanks for using File Organizer")
        greet.setStyleSheet("color: #2f4f4f; font-size: 22px; text-align: center; font-weight: bold;") 

        self.fileOrganizer = QLabel(self)
        pix = QPixmap(path)
        resized =  pix.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.fileOrganizer.setPixmap(QPixmap(resized))
        self.fileOrganizer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bye = QLabel("Exiting.....")
        bye.setStyleSheet("color: #2f4f4f; font-size: 19px; text-align: center; font-weight: bold;")

        layout = QVBoxLayout()
        layout.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fileOrganizer, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bye, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class OrganizeIt(QMainWindow):
    def __init__(self):
        super().__init__()

        path = "C:/Users/aravi/Downloads/folder.png"
        self.setStyleSheet("background-color: #ffa07a;")
        self.setWindowTitle("File Organizer")
        self.setWindowIcon(QIcon(path))

        greet = QLabel("Successfully Organized!!")
        greet.setStyleSheet("color: #2f4f4f; font-size: 22px; text-align: center; font-weight: bold;") 

        self.fileOrganizer = QLabel(self)
        pix = QPixmap(path)
        resized =  pix.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.fileOrganizer.setPixmap(QPixmap(resized))
        self.fileOrganizer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.exit = QPushButton("Exit")
        self.exit.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
        self.exit.setCheckable(True)
        self.exit.setFixedSize(110, 40)
        self.exit.pressed.connect(self.exit_pressed)
        self.exit.released.connect(self.exit_released)
        self.exit.clicked.connect(self.bye)

        layout = QVBoxLayout()
        layout.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fileOrganizer, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.exit, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setFixedSize(500, 500)

    def exit_pressed(self):
        self.exit.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def exit_released(self):
        self.exit.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def bye(self):
        widget.setCurrentIndex(1)
        QTimer.singleShot(1000, self.exit_application)

    def exit_application(self):
        print("Exited Successfully!")
        sys.exit()


app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
window = MainWindow()
close = QuitWindow()
organized = OrganizeIt()

widget.addWidget(window)
widget.addWidget(close)
widget.addWidget(organized)
path = "C:/Users/aravi/Downloads/folder.png"
widget.setStyleSheet("background-color: #ffa07a;")
widget.setWindowTitle("File Organizer")
widget.setWindowIcon(QIcon(path))
widget.setFixedSize(500, 500)
widget.show()

sys.exit(app.exec())
