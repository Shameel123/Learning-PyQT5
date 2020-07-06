from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table! Widget!!")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("Get")

        #-------------Formatting Rows and Colomns----------------------#
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("F.Name"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("Address"))

        # Note: rows/columns number starts from "0"
        self.table.setItem(0,0,QTableWidgetItem("1st Item"))
        self.table.setItem(0,1,QTableWidgetItem("2nd Item"))
        self.table.setItem(1,0,QTableWidgetItem("3rd Item"))
        self.table.setItem(1,1,QTableWidgetItem("4th Item"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) #--------> it restricts fields to be edited!!

        # self.table.horizontalHeader().hide() #in case you want to hide the numbers/names from rows/columns
        # self.table.verticalHeader().hide()

        btn.clicked.connect(self.getValue)
        self.table.doubleClicked.connect(self.doubleClicked) #it allows for the valeus to appear after "DOUBLE CLICK"

        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.show()

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())
    def doubleClicked(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
