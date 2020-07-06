import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Shameel :)")
        self.setGeometry(50,50,200,350)
        text1=QLabel("Label set by Shameel :-) ",self)#self parameter is must to put in order to show it in wondow
        text2=QLabel("Label set by Shameel :-(",self)
        text1.move(0,0)
        text2.move(0,15)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()


