import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
import sqlite3


class MainMenuWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainMenuWidget, self).__init__(parent)
        uic.loadUi('Main_Menu.ui', self)
        self.pushButton_2.clicked.connect(self.open_base_data)

    def open_base_data(self):
        f1 = BaseData(self)
        f1.show()
        self.hide()


class BaseData(QMainWindow):
    def __init__(self, parent=None):
        super(BaseData, self).__init__(parent)
        uic.loadUi('Base_Data.ui', self)
        self.pushButton_2.clicked.connect(self.returned)
        self.pushButton.clicked.connect(self.ex4)
        self.comboBox.hide()

    def ex4(self):
        self.con = sqlite3.connect("PhB.db")
        cur = self.con.cursor()
        a = cur.execute("select name from sqlite_master where type = 'table'").fetchall()
        self.comboBox.show()
        for i in a:
            self.comboBox.addItem(str(i[0]))
        self.comboBox.show()
        self.comboBox.activated[str].connect(self.onChanged)

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize(100, 100)

    def returned(self):
        self.hide()
        ex1 = MainMenuWidget(self)
        ex1.show()


class WriteQue(QMainWindow):
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenuWidget()
    ex.show()
    sys.exit(app.exec_())
