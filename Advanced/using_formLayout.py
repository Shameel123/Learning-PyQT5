import sys
from PyQt5.QtWidgets import *

#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#
#---------Watch video for additional of hbox in the form-----------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("Shameel :)")
        self.setGeometry(50,50,200,350)

        formLayout = QFormLayout()
        #formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)#this is for design and it's up to you!!

        name_txt = QLabel("Name : ")
        name_in  = QLineEdit()
        pass_txt = QLabel("Password : ")
        pass_in  = QLineEdit()

        formLayout.addRow(name_txt,name_in)
        formLayout.addRow(pass_txt,pass_in)
        formLayout.addRow(QLabel("Country"),QComboBox()) #direct arguments.
        formLayout.addRow(QPushButton("Enter"),QPushButton("Cancel"))

        self.setLayout(formLayout)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()


