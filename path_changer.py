# QApplication : the application handler
# QWidget : basic empty GUI widget
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

import sys

# PySide main app class. Inherit windows class.
class MainWindow_class(QtWidgets.QWidget):
    # parent is used when you another window.
    def __init__(self, parent=None):
        # init Base class. In this case it's about QWidget
        super(MainWindow_class,self).__init__(parent=parent)


if __name__ == "__main__":

    # Pass is sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments  QApplication([]) works too.
    app = QApplication(sys.argv)
    
    # Create a Qt widget, which will be our window.
    # Widgets without a parent are invisible by default.
    # All top level widgets are windows. They don't have a parent and are not nested within another widget or layout.
    window = MainWindow_class()

    # Show windows command for PySide6 window.
    # You can remove the .show() and run the app, but you'll have no way to quit it.
    window.show()
    sys.exit(app.exec())
    
    """
    label = QtWidgets.QLabel("Hello", alignment=QtCore.Qt.AlignCenter)
    label.setStyleSheet("font-size:128px;")
    label.show()
    sys.exit(app.exec())
    """