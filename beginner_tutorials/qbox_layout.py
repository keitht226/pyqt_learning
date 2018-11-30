# The purpose of this exercise is to learn how to automatically
# resize widgets within a window using QBox_Layout

import sys
from PyQt5 import QtWidgets

# -----------------------------------------------------------------------------
# Routine: Window
#
# Purpose: Creates a window that, when resized, properly
#          spaces out the buttons in the window
# -----------------------------------------------------------------------------
def window():
  app = QtWidgets.QApplication(sys.argv)
  widget = QtWidgets.QWidget()

  # pb = push button
  pb_top       = QtWidgets.QPushButton("Button1")
  pb_mid       = QtWidgets.QPushButton("Button2")
  pb_bot_left  = QtWidgets.QPushButton("Button3")
  pb_bot_right = QtWidgets.QPushButton("Button4")

  vbox = QtWidgets.QVBoxLayout()
  vbox.addWidget(pb_top)
  vbox.addStretch()
  vbox.addWidget(pb_mid)

  hbox = QtWidgets.QHBoxLayout()
  hbox.addWidget(pb_bot_left)
  hbox.addStretch()
  hbox.addWidget(pb_bot_right)

  vbox.addStretch()
  vbox.addLayout(hbox)
  widget.setLayout(vbox)

  widget.setWindowTitle("PyQt")
  widget.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  window()