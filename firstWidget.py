import re, sys
from PySide6 import QtWidgets
from PySide6 import QtCore


class FirstItemsTable(QtWidgets.QTableView):
    # 先頭から「file:/」
    # 今は使っていないので一次的にコメントアウト
    # RemovePreferLocal = re.compile("^file[:][/]+")

    def __infit__(self, parent=None):
        super(FirstItemsTable, self).__init__(parent=parent)


class FirstWidget(QtWidgets.QWidget):

    def __init__(self,parent=None):
        super(FirstWidget,self).__init__(parent=parent)
        self.__first_table = None
        self.__initialize()

    
    def __initialize(self):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.__test1_radio = QtWidgets.QRadioButton("Test1")
        self.__test2_radio = QtWidgets.QRadioButton("Test2")
        self.__test1_radio.setChecked(True)

        radio_layout = QtWidgets.QHBoxLayout()
        radio_layout.addWidget(self.__test1_radio)
        radio_layout.addWidget(self.__test2_radio)

        box = QtWidgets.QGroupBox()
        box.setLayout(radio_layout)

        self.__first_table = FirstItemsTable()

