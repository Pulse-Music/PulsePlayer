from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import MainWidget
from PyQt6.QtCore import Qt
from sys import exit, argv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.resize(self.mainWidget.size())
        self.setWindowTitle(self.mainWidget.windowTitle())
        self.closeEvent = self.mainWidget.closeEvent

app = QApplication(argv)
window = MainWindow()
app.exec()
