
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from front_end import *


class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.browser.load(QUrl("https://youtube.com"))




if __name__ == "__main__":

    w = QApplication([])
    app = App()
    app.show()
    w.exec_()