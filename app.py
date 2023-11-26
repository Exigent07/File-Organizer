import sys
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
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
        layout.addWidget(self.organize, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.exit, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setFixedSize(500, 500)

    def organize_pressed(self):
        self.organize.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def organize_released(self):
        self.organize.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def exit_pressed(self):
        self.exit.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def exit_released(self):
        self.exit.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def organizing(self):
        organizeFolder()
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

        layout.setContentsMargins(0, 0, 0, 0)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setFixedSize(500, 500)

    def organize_pressed(self):
        self.organize.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def organize_released(self):
        self.organize.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def exit_pressed(self):
        self.exit.setStyleSheet("background-color: #d2b48c; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")
    def exit_released(self):
        self.exit.setStyleSheet("background-color: #f5f5dc; color: #2f4f4f; border-radius: 10px; font-weight: 650; border: 0.5px solid #2f4f4f")

    def organizing(self):
        organizeFolder()
        print("Organized")

app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
window = MainWindow()
close = QuitWindow()

widget.addWidget(window)
widget.addWidget(close)
path = "C:/Users/aravi/Downloads/folder.png"
widget.setStyleSheet("background-color: #ffa07a;")
widget.setWindowTitle("File Organizer")
widget.setWindowIcon(QIcon(path))
widget.setFixedSize(500, 500)
widget.show()

sys.exit(app.exec())
