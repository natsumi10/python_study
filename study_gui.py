import sys
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

class MainWindow(QtWidgets.QMainWindow):
    print ("start")
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent=parent)
        self.__initialize()
    
    def __initialize(self):
        center = QtWidgets.QWidget()
        # QVBoxLayout : 垂直方向にウィジェットを並べる。（水平はQHBoxLayout）
        layout = QtWidgets.QVBoxLayout()
        center.setLayout(layout)

        # 全体を格納する為のウィジェット。必須。
        self.setCentralWidget(center)


if __name__ == "__main__":
    print ("start")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())