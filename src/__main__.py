from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt6.uic import loadUi
from qt_material import list_themes, apply_stylesheet
from utility import (
    load_settings,
    save_settings,
)
import sys, os


class UserInterface(QMainWindow):
    def __init__(self, ChangeWindowFunc):
        super().__init__()
        self.setWindowCaption("Loading...")
        self.settings = load_settings("settings.yml")
        self.changewindow = ChangeWindowFunc
        self.initUI()
        self.setWindowCaption()
        self.show()

    def initUI(self):
        # Load the UI from the .ui file
        loadUi(os.path.abspath("assets/layout.ui"), self)
        # Set the theme
        # FIXME: The theme library doesn't properly work with UI files

    def setWindowCaption(self, caption: str = None):
        if caption is not None:
            self.setWindowTitle("Pulse Player - %s" % caption)
        else:
            self.setWindowTitle("Pulse Player")

    def setTheme(self, theme: str):
        EXTRA = dict(
            density_scale=str(self.settings["scale"]),
        )
        try:
            apply_stylesheet(self, theme.replace(" ", "_") + ".xml", extra=EXTRA)
            self.settings["theme"] = theme
        except Exception as e:
            # Print the full traceback

            apply_stylesheet(self, "dark_cyan.xml")
            self.settings["theme"] = "Dark Cyan"


    def saveSettings(self):
        self.logger.info("Saving settings")
        save_settings("settings.yml", self.settings)


def main():
    app = QApplication(sys.argv)
    UI = UserInterface(ChangeWindowFunc=app.setActiveWindow)
    app.setActiveWindow(UI)
    EXIT_CODE = app.exec()
    sys.exit(EXIT_CODE)


if __name__ == "__main__":
    main()
