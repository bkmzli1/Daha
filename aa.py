from PyQt5 import uic, QtWidgets
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMainWindow, QWidget, QPushButton

import ServerConnect
import data


def labels(label: QtWidgets.QLabel):
    return label


def button(button: QtWidgets.QPushButton):
    return button


def text(lineEdit: QtWidgets.QLineEdit):
    return lineEdit


def comboBox(lineEdit: QtWidgets.QComboBox):
    return lineEdit


class UiMain(QWidget):
    def __init__(self):
        super(UiMain, self).__init__()
        uic.loadUi('MainPage.ui', self)

        label = labels(self.label)
        pushButton = button(self.pushButton)
        pushButton.clicked.connect(lambda: self.button_clic())

    def button_clic(self):
        data.loginJson = ServerConnect.connect(
            '{ "type":"auth","userName":"' + text(self.name).text() + '","password":"' + text(
                self.password).text() + '" }')
        if data.loginJson:
            self.w2 = UiStud()
            self.w2.show()
            self.close()


class UiStud(QWidget):
    def __init__(self):
        super(UiStud, self).__init__()

        if data.loginJson['role'] == 'PREPOD':
            uic.loadUi('Teachers_View__creating_new_sub.ui', self)

            creatingSubjectSubmit = button(self.creatingSubjectSubmit)
            creatingSubjectSubmit.clicked.connect(lambda: self.button_clic())
        else:
            uic.loadUi('StudentsView.ui', self)
            name = labels(self.name)
            name1 = labels(self.name2)
            name2 = labels(self.name3)
            print(data.loginJson)
            name.setText(data.loginJson['user_name'])
            name1.setText(data.loginJson['surname'])
            name2.setText(data.loginJson['patronymic'])
        self.setWindowTitle('SecondWindow')

    def button_clic(self):
        self.w2 = UiCreatingSubject()
        self.w2.show()
        self.close()


class UiCreatingSubject(QWidget):
    def __init__(self):
        super(UiCreatingSubject, self).__init__()
        uic.loadUi('CreatingSubject.ui', self)
        teacherChoose = comboBox(self.TeacherChoose)
        prepods = ServerConnect.connect(
            '{ "type":"prepod","userName":"' + data.loginJson['name'] + '","password":"' + data.loginJson[
                'password'] + '","role":"PREPOD" }')
        for item in prepods.keys():
            teacherChoose.addItem(
                prepods[item]['user_name'] + ' ' + prepods[item]['surname'] + ' ' + prepods[item]['patronymic'])
        TeacherChoose = comboBox(self.TeacherChoose)
        creatingCodeSubject_2 = comboBox(self.creatingCodeSubject_2)
        creatingSubjectSubmit = button(self.creatingSubjectSubmit)
        creatingSubjectSubmit.clicked.connect(lambda: self.button_clic())
    def button_clic(self):




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UiMain()
    window.show()
    sys.exit(app.exec_())
