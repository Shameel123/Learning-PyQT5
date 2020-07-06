import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(50,50,500,350)
        self.button = QPushButton("ENTER THE TEXT!",self)
        self.button.move(180,280)

        self.textEditor = QTextEdit(self)
        self.textEditor.setAcceptRichText(True)
        self.button.clicked.connect(self.copyText)
        self.show()

    def copyText(self):
        text = self.textEditor.toPlainText()
        print(text)

def main():
    App = QApplication(sys.argv)
    win = myWindow()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
