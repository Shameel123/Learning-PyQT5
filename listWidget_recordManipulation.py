
import sys
from PyQt5.QtWidgets import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(50,50,400,300)
        self.setWindowTitle("Shameel's Window!!! Don't Enter!")
        self.label = QLabel("Shameel's List Manipulation Program",self)
        self.label.move(100,0)
        #---------------Buttons----------------------#
        button1 = QPushButton("Add",self)
        button2 = QPushButton("Delete",self)
        button3 = QPushButton("Get",self)
        button4 = QPushButton("Delete All",self)

        button1.move(280,60)
        button2.move(280,90)
        button3.move(280,120)
        button4.move(280,150)

        button1.clicked.connect(self.add)
        button2.clicked.connect(self.delete)
        button3.clicked.connect(self.get)
        button4.clicked.connect(self.deleteAll)

        #------------Line Edit------------------------
        self.edit = QLineEdit(self)
        self.edit.move(20,25)
        #------------List-Widget----------------------#
        # lst = ["Superman","Batman","Joker","Flash"]
        self.listWidget = QListWidget(self)
        # self.listWidget.addItems(lst)
        self.listWidget.move(20,50)

        self.show()

    def add(self):
        val = self.edit.text()
        self.listWidget.addItem(val)
        self.edit.setText("") #sets the line edit to be null once the value has been entererd

    def delete(self):
        id=self.listWidget.currentRow()
        self.listWidget.takeItem(id)

    def deleteAll(self):
        self.listWidget.clear()

    def get(self):
        val = self.listWidget.currentItem().text()
        print(val)

def main():
    app = QApplication(sys.argv)
    window = myWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
