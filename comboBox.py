import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Shameel :)")
        self.setGeometry(50,50,160,200)
        self.comboBox = QComboBox(self)
        self.comboBox.move(50,50)
        #self.comboBox.addItems(["Shameel" ,"Uddin"])
        lst = ["Choose","Shameel","Uddin"]
        self.comboBox.addItems(lst)

        self.text = QLabel("",self)

        button = QPushButton("OK!",self)
        button.clicked.connect(self.getComboBox)



        self.show()

    def getComboBox(self):
        value = self.comboBox.currentText()
        if value!= "Choose":
            self.text.setText(value)
            self.text.move(60,80)
            self.text.adjustSize()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()


