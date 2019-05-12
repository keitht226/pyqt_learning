import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()
    grid = QtWidgets.QGridLayout()

    for i in range(1, 5):
        for j in range(1, 5):
            button_num = j + 4 * (i - 1)
            grid.addWidget(QtWidgets.QPushButton("B" + str(button_num)), i, j)

    win.setLayout(grid)
    win.setGeometry(100, 100, 200, 100)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
