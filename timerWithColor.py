import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(50,50,500,200)
        self.setWindowTitle("Shameel's Window!!! Don't Enter!")
        #-------------Color---------------------------------#
        self.color = QLabel(self)
        self.color.setStyleSheet("background-color:green")
        #------------------Buttons-------------------------#
        button1 = QPushButton("Shameel Enter",self)
        button2 = QPushButton("Uddin Exit",self)
        button1.move(10,30)
        button2.move(100,30)
        button1.clicked.connect(self.enterFunc)
        button2.clicked.connect(self.exitFunc)
        #------------------Timer---------------------------#
        self.timer = QTimer()
        self.timer.timeout.connect(self.changeColor)

        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        # I have left this code because it was boring, copy it from lectures
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#
        #---------------------------------------------------#

        self.show()

    def enterFunc(self):
        pass
    def exitFunc(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = myWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
