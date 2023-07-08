import sys
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

import firstWidget

import logging
# ログの出力名を設定
logger = logging.getLogger(__name__)
# ログレベルの設定
logger.setLevel(10)

# ログのコンソール出力の設定
logOnTermins = logging.StreamHandler()
logger.addHandler(logOnTermins)

# ログのファイル出力先を設定
logOnTxtFile = logging.FileHandler("loggingText.log")
logger.addHandler(logOnTxtFile)

# ログの出力形式の設定
# 実行時間(年-月-日 時-分-秒,ミリ秒) - 行番号 出力名 : ログレベル名 - メッセージ文字列
formatter = logging.Formatter('%(asctime)s - Line %(lineno)d %(name)s : %(levelname)s: - %(message)s')
logOnTermins.setFormatter(formatter)
logOnTxtFile.setFormatter(formatter)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent=parent)
        self.__first_widget = None
        self.__initialize()
    
    def __initialize(self):
        center = QtWidgets.QWidget()
        # QVBoxLayout : 垂直方向にウィジェットを並べる。（水平はQHBoxLayout）
        layout = QtWidgets.QVBoxLayout()
        # setLayout メソッド、親ウィジェットにレイアウトを設定する。
        center.setLayout(layout)

        # 全体を格納する為のウィジェット。必須。
        self.setCentralWidget(center)

        self.__first_widget = firstWidget.FirstWidget()


if __name__ == "__main__":
    logger.info("main start")

    """ logging examples"""
    logger.log(20,"log for messages")
    logger.log(30, "log for warning")
    logger.log(100,"log for test")
    logger.warning("warning test")
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())