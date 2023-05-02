from PySide2.QtWidgets import QApplication, QWidget, QDialog, QLineEdit, QPushButton

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec_()