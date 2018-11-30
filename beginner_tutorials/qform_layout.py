import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()

    fbox = QtWidgets.QFormLayout()

    # add Name field
    l1 = QtWidgets.QLabel("Name")
    name = QtWidgets.QLineEdit()
    fbox.addRow(l1, name)

    # Add 2 line address field
    l2 = QtWidgets.QLabel("Address")
    add1 = QtWidgets.QLineEdit()
    add2 = QtWidgets.QLineEdit()
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(add1)
    vbox.addWidget(add2)
    fbox.addRow(l2, vbox)

    # Add gender radio selection
    radio1 = QtWidgets.QRadioButton("Male")
    radio2 = QtWidgets.QRadioButton("Female")
    hbox = QtWidgets.QHBoxLayout()
    hbox.addWidget(radio1)
    hbox.addWidget(radio2)
    # Prevents radio2 from stretching far from radio1 with resize of window
    hbox.addStretch()
    fbox.addRow(QtWidgets.QLabel("sex"), hbox)

    # Add Submit and Cancel Buttons
    hbox = QtWidgets.QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(QtWidgets.QPushButton("Submit"))
    hbox.addWidget(QtWidgets.QPushButton("Cancel"))
    fbox.addRow(hbox)

    win.setLayout(fbox)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()