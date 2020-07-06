import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Shameel :)")
        self.setGeometry(50,50,160,200)
        self.myLineEdit1 = QLineEdit(self)
        self.myLineEdit1.move(12,0)
        self.myLineEdit1.setPlaceholderText("Username")
        self.myLineEdit2 = QLineEdit(self)
        self.myLineEdit2.move(12,20)
        self.myLineEdit2.setPlaceholderText("Password")
        self.myLineEdit2.setEchoMode(QLineEdit.Password)
        self.button1 = QPushButton("Enter",self)
        self.button1.move(37,60)
        self.button1.clicked.connect(self.doSth)
        self.checkBox = QCheckBox("Appear on Screen",self)
        self.checkBox.move(13,40)
        self.user = QLabel("",self)
        self.pswd = QLabel("",self)
        self.user.move(17,80)
        self.pswd.move(17,100)
        self.show()

    def doSth(self):
        if (self.checkBox.isChecked()):
            self.user.setText(self.myLineEdit1.text())
            self.pswd.setText(self.myLineEdit2.text())
            self.user.adjustSize()
            self.pswd.adjustSize()

        else:
            self.user.setText("")
            self.pswd.setText("")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()


