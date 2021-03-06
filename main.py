# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime
sqliteConnection = sqlite3.connect('db.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = sqliteConnection.cursor()
from collection.add import Add1,Add2
from collection.display import Display1, Display2
from collection.update import Update1, Update2
from collection.delete import delete1
import collection.management 






class Home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(60, 40, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(a)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(400, 40, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(b)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(60, 240, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(c)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(400, 240, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(d)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.button1.setText(_translate("MainWindow", "Update"))
        self.button2.setText(_translate("MainWindow", "List Of Passangers"))
        self.button3.setText(_translate("MainWindow", "Add Flight"))
        self.button4.setText(_translate("MainWindow", "Delete Flight"))
def data(self):
    f = "once"
    name = self.comboBox_2.currentText()
    if name=="":
        text = "No Flight Name Entered"
        self.er(text)
        return
    d = "d"
    if self.radioButton.isChecked():
        d = "a"
    no = value = self.lineEdit.text()
    if no=="":
        text = "enter flight no."
        self.er(text)
        return
    global dtemp 
    dtemp = [f,name,d,no]
    print(f,name,d,no)
    ui = Add2()
    ui.setupUi(MainWindow, data2,dtemp)
    MainWindow.show()

def data2(self):
        airport = self.comboBox_2.currentText()
        if airport=="gggg":
            text = "No Airport Name Entered"
            self.er(text)
            return
        s = self.dateTimeEdit_2.dateTime()
        s = s.toPyDateTime()
        f = self.dateTimeEdit.dateTime()
        f = f.toPyDateTime()
        ec = 0
        bs = 0
        if dtemp[2]=="d":
            ec = self.lineEdit.text()
            bs = self.lineEdit_2.text()
        print(airport,s,f,ec,bs)
        collection.management.insert_flight_details(cursor,dtemp[3],dtemp[1],airport,dtemp[2],s,f,ec,bs)
        sqliteConnection.commit()
        ui = Home()
        ui.setupUi(MainWindow)
        MainWindow.show()
def data3(pk):
    data = collection.management.show_passanger(cursor, pk)
    ui = Display2()
    ui.setupUi(MainWindow, data,b)
    MainWindow.show()

def data4(pk):
    ui = Update2()
    ui.setupUi(MainWindow,pk,u_cost,delay,cancel,a)
    MainWindow.show()

def data5(pk):
    collection.management.delete(cursor,pk)
    sqliteConnection.commit()
    d()

def cancel(self,pk):
    collection.management.cancel(cursor,pk)
    sqliteConnection.commit()
    a()

def delay(self,pk):
    t = self.lineEdit_3.text()
    collection.management.delay(cursor,pk,t)
    sqliteConnection.commit()
    a()

def u_cost(self,pk):
    e = self.lineEdit.text()
    bu = self.lineEdit_2.text()
    collection.management.u_cost(cursor,pk,e,bu)
    sqliteConnection.commit()
    a()

def to_home():
    ui = Home()
    ui.setupUi(MainWindow)
    MainWindow.show()

def a():
    print("a")
    ui = Update1()
    data = collection.management.show_flight(cursor)
    print(data)
    ui.setupUi(MainWindow, data,data4,to_home)
    MainWindow.show()

def b():
    print("b")
    ui = Display1()
    data = collection.management.show_flight(cursor)
    print(data)
    ui.setupUi(MainWindow, data,data3,to_home)
    MainWindow.show()

def c():
    print("c")
    ui = Add1()
    ui.setupUi(MainWindow,data)
    MainWindow.show()

def d():
    print("d")
    ui = delete1()
    data = collection.management.show_flight(cursor)
    print(data)
    ui.setupUi(MainWindow, data,data5,to_home)
    MainWindow.show()
class MaiWindow(QtWidgets.QMainWindow, Home):
    def __init__(self, parent=None):
        super(MaiWindow, self).__init__(parent=parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MaiWindow()
    MainWindow.show()
    sys.exit(app.exec_())
    sqliteConnection.commit()
    sqliteConnection.close()
