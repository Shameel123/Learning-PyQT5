from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab! Widget!!")
        self.setGeometry(350,150,300,300)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.editor = QTextEdit() #<--- denotes that we can open and narrate txt files

        fileButton = QPushButton("Open File")
        fontButton = QPushButton("Font Button")
        colorButton= QPushButton("Color Button")

        fileButton.clicked.connect(self.openFile)
        fontButton.clicked.connect(self.changeFont)
        colorButton.clicked.connect(self.changeColor)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addWidget(fontButton)
        hbox.addWidget(colorButton)
        hbox.addStretch()
        self.setLayout(vbox)

        self.show()

    def openFile(self):
        url = QFileDialog.getOpenFileName(self,"Open File","","All Files(*);;*txt")
        print(url)
        fileUrl = url[0]
        print(fileUrl)
        file = open(fileUrl,'r')
        content = file.read()
        self.editor.setText(content)

    def changeFont(self):
        font,ok = QFontDialog.getFont() # i dont quite understand this part.. don't know why we use 2 variables :-)
        if ok:
            self.editor.setCurrentFont(font)
    def changeColor(self):
        color  = QColorDialog.getColor()
        self.editor.setTextColor(color)

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
