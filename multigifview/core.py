from mainwindow import Ui_MainWindow
from Qt.QtWidgets import QMainWindow


class MultiGifView(QMainWindow, Ui_MainWindow):
    """A program for viewing .gif files"""

    def __init__(self, args):
        super().__init__(None)
        self.setupUi(self)


