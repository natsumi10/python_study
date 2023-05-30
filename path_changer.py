import PySide6
from PySide6 import QtCore, QtWidgets, QApplication

import os
import sys

# PySide main app class. Inherit windows class.
class MainWindow_class(QWidget):
    # parent is used when you another window.
    def __init__(self, paret=None):
        # init Base class. In this case it's about QWidget
        super().__init__(parent)

if __name__ == "__main__":
    # Register PySide6 to env variables
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    print ("sys.argv is : ", sys.argv)
    
    # Execute PySide6
    app = QApplication(sys.argv)
    window = MainWindow_class()
    # Show windows command for PySide6 window.
    window.show()
    sys.exit(app.exec())

    """
    label = QtWidgets.QLabel("Hello", alignment=QtCore.Qt.AlignCenter)
    label.setStyleSheet("font-size:128px;")
    label.show()
    sys.exit(app.exec())
    """