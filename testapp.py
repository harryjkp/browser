import sys, PySide2, random

from PySide2.QtWidgets import QApplication, QLabel
from PySide2 import QtCore, QtWidgets, QtGui



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.input = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("Click me!")
        self.button2 = QtWidgets.QPushButton("Fetch Webpage!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)


        # Search box
        self.layout2 = QtWidgets.QHBoxLayout()
        self.layout2.addWidget(self.input)
        self.layout2.addWidget(self.button2)

        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addLayout(self.layout2)


        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))



if __name__ == "__main__":

    app = QApplication(sys.argv)


    widget = MyWidget()
    widget.resize(800, 600)

    widget.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    widget.show()


    #label = QLabel("Hello World")

    #label.show()


    # Prints PySide2 version
    # e.g. 5.11.1a1
    print(PySide2.__version__)

    # Gets a tuple with each version component
    # e.g. (5, 11, 1, 'a', 1)
    print(PySide2.__version_info__)

    # Prints the Qt version used to compile PySide2
    # e.g. "5.11.2"
    print(PySide2.QtCore.__version__)

    # Gets a tuple with each version components of Qt used to compile PySide2
    # e.g. (5, 11, 2)
    print(PySide2.QtCore.__version_info__)
    sys.exit(app.exec_())
