import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLineEdit, QInputDialog
import sqlite3


class MainMenuWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainMenuWidget, self).__init__(parent)
        uic.loadUi('Main_Menu.ui', self)
        self.pushButton_2.clicked.connect(self.open_base_data)
        self.pushButton.clicked.connect(self.open_generate_work)

    def open_base_data(self):
        f1 = BaseData(self)
        f1.show()
        self.hide()

    def open_generate_work(self):
        f = CreateWork(self)
        f.show()
        self.hide()


class BaseData(QMainWindow):
    def __init__(self, parent=None):
        super(BaseData, self).__init__(parent)
        uic.loadUi('Base_Data.ui', self)
        self.pushButton_2.clicked.connect(self.returned)
        self.pushButton.clicked.connect(self.ex4)
        self.pushButton_3.clicked.connect(self.add_theme)
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
        self.con.close()

    def onChanged(self, text):
        self.hide()
        a = WriteQue(self, text)
        a.show()

    def returned(self):
        self.hide()
        ex1 = MainMenuWidget(self)
        ex1.show()

    def add_theme(self):
        text, ok = QInputDialog.getText(self, 'Добавить раздел',
                                        'Введите название')
        if ok:
            con = sqlite3.connect("PhB.db")
            cur = con.cursor()
            a = "CREATE TABLE " + text + "(body STRING NOT NULL);"
            cur.execute(a)
            con.commit()
            con.close()


class WriteQue(QMainWindow):
    def __init__(self, parent=None, text=None):
        super(QMainWindow, self).__init__(parent)
        uic.loadUi('Write_Que.ui', self)
        self.text = text
        self.pushButton.clicked.connect(self.save_result)
        self.spinBox.hide()
        self.spinBox_2.hide()
        self.spinBox_3.hide()
        self.spinBox_4.hide()
        self.spinBox_5.hide()
        self.spinBox_6.hide()
        self.spinBox_7.hide()
        self.spinBox_8.hide()
        self.spinBox_9.hide()
        self.spinBox_10.hide()
        self.label_1.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.pushButton_2.clicked.connect(self.ready)

    def save_result(self):
        con = sqlite3.connect("PhB.db")
        cur = con.cursor()
        a = "INSERT INTO " + self.text + "(body) VALUES(" + '"'\
            + self.plainTextEdit.toPlainText() + '"' + ')'
        cur.execute(a)
        con.commit()
        con.close()
        self.close()
        a = MainMenuWidget(self)
        a.show()

    def activ_1(self):
        self.spinBox.show()
        self.spinBox_2.show()
        self.label_1.show()
        self.label_2.show()
        self.label_3.show()

    def activ_2(self):
        self.activ_1()
        self.spinBox_3.show()
        self.spinBox_4.show()
        self.label_4.show()
        self.label_5.show()
        self.label_6.show()

    def activ_3(self):
        self.activ_2()
        self.spinBox_5.show()
        self.spinBox_6.show()
        self.label_7.show()
        self.label_8.show()
        self.label_9.show()
    def activ_4(self):
        self.activ_3()
        self.spinBox_7.show()
        self.spinBox_8.show()
        self.label_7.show()
        self.label_8.show()
        self.label_10.show()
        self.label_11.show()
        self.label_12.show()

    def activ_5(self):
        self.activ_4()
        self.spinBox_9.show()
        self.spinBox_10.show()
        self.label_13.show()
        self.label_14.show()
        self.label_15.show()

    def ready(self):
        text = self.plainTextEdit.toPlainText()
        if text.count('!') == 5:
            self.activ_5()
        elif text.count('!') == 4:
            self.activ_4()
        elif text.count('!') == 3:
            self.activ_3()
        elif text.count('!') == 2:
            self.activ_2()
        elif text.count('!') == 1:
            self.activ_1()

class CreateWork(QMainWindow):
    def __init__(self, parent=None):
        super(CreateWork, self).__init__(parent)
        uic.loadUi('Generate_Work.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenuWidget()
    ex.show()
    sys.exit(app.exec_())
