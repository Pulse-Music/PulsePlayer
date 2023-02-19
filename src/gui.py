from PyQt6.QtWidgets import QWidget
from PyQt6 import QtGui
from PyQt6.uic import loadUi

class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()


    def setup_ui(self):
        loadUi("res/GUI/main.ui", self)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("Closing the main widget")
        a0.accept()