import sys
from PyQt5.QtWidgets import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()



    def UI(self):
        self.setWindowTitle("Shameel learning Horizontal Layour")
        self.setGeometry(450,150,400,400)




        self.b1 = QPushButton("Button 1")
        self.b2 = QPushButton("Button 2")
        self.b3 = QPushButton("Button 3")


        self.vbox = QVBoxLayout()

        self.vbox.addStretch()
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)


        self.show()

def main():
    app = QApplication(sys.argv)
    win = myWindow()
    sys.exit(app.exec_())


if __name__ =="__main__":
    main()

