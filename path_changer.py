import PySide6
from PySide6 import QtCore
from PySide6 import QtWidgets
import os
import sys

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

app = QtWidgets.QApplication()
label = QtWidgets.QLabel("Hello", alignment=QtCore.Qt.AlignCenter)
label.setStyleSheet("font-size:18px;")
label.show()
sys.exit(app.exec())