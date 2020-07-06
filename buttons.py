import sys
from PyQt5.QtWidgets import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(50,50,500,200)
        self.setWindowTitle("Shameel's Window!!! Don't Enter!")
        self.text = QLabel("Shameel trying Buttons ;)",self)
        button1 = QPushButton("Shameel Enter",self)
        button2 = QPushButton("Uddin Exit",self)
        self.text.move(17,0)
        button1.move(10,30)
        button2.move(100,30)

        button1.clicked.connect(self.enterFunc)
        button2.clicked.connect(self.exitFunc)

        self.show()

    def enterFunc(self):
        self.text.setText("Why did you Enter?!?!?!")
        self.text.resize(150,20)
    def exitFunc(self):
        self.text.setText("Noooo!! Don't EXIT!!!!")
        self.text.resize(150,20)
def main():
    app = QApplication(sys.argv)
    window = myWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
