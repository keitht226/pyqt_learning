import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def window(start_position_x, start_position_y):
  app = QtWidgets.QApplication(sys.argv)
  dialog = QtWidgets.QDialog()
  top_button = QtWidgets.QPushButton(dialog)
  top_button.setText("Top Button")
  top_button.move(50, 20)
  top_button.clicked.connect(top_button_clicked)

  bottom_button = QtWidgets.QPushButton(dialog)
  bottom_button.setText("Bottom Button")
  bottom_button.move(50, 50)
  bottom_button.clicked.connect(bottom_button_clicked)

  dialog.setGeometry(start_position_x, start_position_y, 200, 100)
  dialog.setWindowTitle("PyQt")
  dialog.show()
  sys.exit(app.exec_())

def top_button_clicked():
  print ("Top But Pressed")

def bottom_button_clicked():
  print ("Bot But Pressed")

if __name__=='__main__':
  window(500, 500)