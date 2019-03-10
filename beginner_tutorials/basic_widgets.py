"""
Overview of most common Widgets
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class WidgetsOverview(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self._app = app

        win = QWidget()
        self.setCentralWidget(win)
        form = QFormLayout()

        # QLineEdit
        label = QLabel("QLineEdit")
        line_edit = QLineEdit()
        form.addRow(label, line_edit)

        # QPushButton
        label = QLabel("QPushButton")
        pb = QPushButton("Push Button")
        form.addRow(label, pb)

        # QRadioButton
        label = QLabel("QRadioButton")
        rb = QRadioButton("radio button")
        form.addRow(label, rb)

        # QCheckBox
        label = QLabel("QCheckBox")
        cb = QCheckBox("Check Box")
        form.addRow(label, cb)

        # QComboBox
        label = QLabel("QComboxBox")
        combo_box = QComboBox()
        combo_box.addItem("Item1")
        combo_box.addItem("Item2")
        combo_box.addItems(["Item3", "Item4"])
        form.addRow(label, combo_box)

        # QSpinBox
        label = QLabel("QSpinBox")
        spin_box = QSpinBox()
        form.addRow(label, spin_box)

        # QSlider Widget
        label = QLabel("QSlider")
        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(10)
        slider.setValue(5)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        form.addRow(label, slider)

        # QMenuBar, QMenu & QAction
        # No need to layout a menubar. It automatically sets its own geometry
        # to the top of the parent widget and changes it appropriately
        # whenever the parent is resized.
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        file_menu.addAction("New")

        file_save = QAction("Save", self)
        file_save.setShortcut("Ctrl+S")
        file_menu.addAction(file_save)

        file_edit = file_menu.addMenu("Edit")
        file_edit.addAction("copy")
        file_edit.addAction("paste")

        file_quit = QAction("Quit", self)
        file_menu.addAction(file_quit)
        file_menu.triggered[QAction].connect(self.close)

        win.setLayout(form)
        win.setWindowTitle("Widget Summary")


def main():
    app = QApplication(sys.argv)
    window = WidgetsOverview(app)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
