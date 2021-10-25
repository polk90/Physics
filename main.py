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
        self.comboBox.activated[str].connect(self.on_changed)
        self.con.close()

    def on_changed(self, text):
        self.write_que(text)

    def returned(self):
        self.hide()
        ex1 = MainMenuWidget(self)
        ex1.show()

    def write_que(self, text):
        self.hide()
        f = WriteQue(self, text)
        f.show()


    def give_tb(self):
        return self.table_n


class WriteQue(QMainWindow):
    def __init__(self, parent=None, table=None):
        super(WriteQue, self).__init__(parent)
        self.table_name = table
        uic.loadUi('Add_Que.ui', self)
        self.pushButton.clicked.connect(self.save_button)

    def save_button(self):
        text = self.plainTextEdit.toPlainText()
        self.con = sqlite3.connect("PhB.db")
        cur = self.con.cursor()
        idd = cur.execute('select count(*) from ' + self.table_name).fetchone()[0] + 1
        to_execute = self.table_name + '(id, name) VALUES(' + str(idd) + ',' + '"' + text + '")'
        a = 'INSERT INTO ' + to_execute
        cur.execute(a)
        self.con.commit()
        self.con.close()
        self.close()
        ex = BaseData(self)
        ex.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenuWidget()
    ex.show()
    sys.exit(app.exec_())
