import sys
from PyQt5 import QtWidgets

def window():
  app = QtWidgets.QApplication(sys.argv)
  widget = QtWidgets.QWidget()
  label = QtWidgets.QLabel(widget)
  label.setText("Hello World!")
  widget.setGeometry(1000, 700, 400, 100)
  label.move(200,50)
  widget.setWindowTitle("PyQt")
  widget.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  window()