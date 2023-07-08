import re
from PySide6 import QtWidgets


class FirstItemsTable(QtWidgets.QTableView):
    # 先頭から「file:/」
    RemovePreferLocal = re.compile("^file[:][/]+")

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

