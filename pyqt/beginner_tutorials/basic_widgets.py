"""
Overview of most common Widgets
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class WidgetsOverview(QMainWindow):
    def __init__(self, app):
        # Initialize parent without knowing its name
        super().__init__()

        self._app = app
        self.setWindowTitle("Widget Summary")

        # QTab
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tab1UI()
        self.tab2UI()
        self.setCentralWidget(self.tabs)

    def tab1UI(self):
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
        spin_box.setRange(0, 10)
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
        # Note that the only action
        # connected to any of these buttons is to exit the program
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

        # QToolBar
        # Can pass fallback into fromTheme as well if available
        # Note that no actions are assigned to these buttons
        toolbar = self.addToolBar("File")

        new = QAction(QtGui.QIcon.fromTheme("new"), "new", self)
        toolbar.addAction(new)

        save = QAction(QtGui.QIcon.fromTheme("save"), "save", self)
        toolbar.addAction(save)

        # QInput Dialog
        btn = QPushButton("Choose from list")
        btn.clicked.connect(self.getItem)
            
        self.le = QLineEdit()
        form.addRow(btn,self.le)
        btn1 = QPushButton("get name")
        btn1.clicked.connect(self.gettext)
            
        self.le1 = QLineEdit()
        form.addRow(btn1,self.le1)
        btn2 = QPushButton("Enter an integer")
        btn2.clicked.connect(self.getint)
            
        self.le2 = QLineEdit()
        form.addRow(btn2,self.le2)

        # QFontDialog
        # Font selector widget. Probaly best to just leave it to 
        # system font rather than overriding.

        # QFileDialog
        label = QLabel("QFileDialog")
        btn = QPushButton("Open File")
        btn.clicked.connect(self.getfile)
        form.addRow(label, btn)

        # QStacked
        # Provides stack of widgets, only one of which can have focus

        # QSplitter
        # Provides resizable sections within widget

        # Dockable
        # Provides a dockable / undockable section within a widget

        # QStatusBar
        # Provides a permanent status bar at the bottom of the widget

        # QListWidget
        # Item-based interface to add or remove items from a list.
        # Each item is a QListWidgetItem object.
        # Items can be multi-selectable

        # QScrollBar
        # Adds scroll bar

        # QCalendarWidget
        # Adds calendar for selcting dates.

        # Finally, set the layout
        self.tab1.setLayout(form)

    def tab2UI(self):
        form = QFormLayout()
        self.tab2.setLayout(form)
        return
            
    def getItem(self):
        items = ("C", "C++", "Java", "Python")
            
        # getItem(self, title, label, list, current=0, editable=True, flags=0)
        # returns True if ok is pressed, False if cancel is pressed
        item, ok = QInputDialog.getItem(self, "select input dialog", 
            "list of languages", items, 0, False)
                
        if ok and item:
            self.le.setText(item)
                
    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
            
        if ok:
            self.le1.setText(str(text))
                
    def getint(self):
        num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number")
            
        if ok:
            self.le2.setText(str(num))
    
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Data Files (*.csv *.txt)")
        return fname

def main():
    app = QApplication(sys.argv)
    window = WidgetsOverview(app)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
