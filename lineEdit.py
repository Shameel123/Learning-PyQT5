import sys
from PyQt5.QtWidgets import *

class myWindow(QWidget):
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
        self.button1.move(37,40)
        self.button1.clicked.connect(self.doSth)
        self.text = QLabel("",self)
        self.show()

    def doSth(self):
        self.username = self.myLineEdit1.text()
        self.password = self.myLineEdit2.text()
        self.text.setText("{} <-- wut iz diz?!".format(self.password))
        self.text.move(0,80)
        self.text.adjustSize()

def main():
    app = QApplication(sys.argv)
    window = myWindow()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
