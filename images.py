import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(''))
        self.image.move(0,0)
        self.setGeometry(50,50,500,350)
        self.showButton = QPushButton("Show Me!!!",self)
        self.stopButton = QPushButton("HIDEEE!!!!",self)
        self.showButton.move(150,280)
        self.stopButton.move(250,280)
        self.showButton.clicked.connect(self.showFunc)
        self.stopButton.clicked.connect(self.stopFunc)

        self.show()

    def showFunc(self):
        self.image.setPixmap(QPixmap('images\car.png'))
        self.image.adjustSize()

    def stopFunc(self):
        self.image.setPixmap(QPixmap(''))

def main():
    App = QApplication(sys.argv)
    win = myWindow()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
