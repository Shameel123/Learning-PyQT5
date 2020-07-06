import sys
from PyQt5.QtWidgets import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(50,50,500,200)
        self.setWindowTitle("Shameel's Window!!! Don't Enter!")
        self.text = QLabel("",self)
        self.button1 = QPushButton("Show/Hide",self)
        self.text.move(17,0)
        self.button1.move(10,30)

        self.spinBox = QSpinBox(self)
        self.spinBox.move(150,50)
        # self.spinBox.setMaximum(100)
        # self.spinBox.setMinimum(0)
        self.spinBox.setRange(10,110)
        self.spinBox.setPrefix("$")
        #self.spinBox.valueChanged.connect(self.enterFunc)

        self.button1.clicked.connect(self.enterFunc)

        self.counter = 0

        self.show()

    def enterFunc(self):
        self.counter += 1
        print(self.counter)
        if self.counter%2!=0:
            value = self.spinBox.value()
            val2  = str(value)
            self.text.setText(val2)
            self.text.resize(150,20)
        else:
            self.text.setText("")


def main():
    app = QApplication(sys.argv)
    window = myWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
