# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from collection.combo import ExtendedComboBox
import json
f=open("list.json","r")
r = json.load(f)
g = r[0]
r = r[1]
f.close()
list_ = [ j for j, i in g ]

class Add1(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 112, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 20, 112, 23))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 90, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setItalic(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 310, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: data(self))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = ExtendedComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 170, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        for i in r:
            self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 240, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 241, 17))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Arrival"))
        self.radioButton_2.setText(_translate("MainWindow", "Departure"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Once"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Daily"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Weekly"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Monthly"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.label.setText(_translate("MainWindow", "Frequence"))
        for i in range(0,len(r)):
            self.comboBox_2.setItemText(i+1, _translate("MainWindow", list_[i]))
        self.label_2.setText(_translate("MainWindow", "Select/Search Airline Name :"))
        self.label_3.setText(_translate("MainWindow", "Flight No."))

    def er(self,t):
        self.label_4.setText(t)

class Add2(object):
    def setupUi(self, MainWindow,data2,d):
        self.d = d;
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(190, 160, 194, 26))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(190, 90, 194, 26))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = ExtendedComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 20, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        for i in list_:
            self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        if d[2]=="d":
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit.setGeometry(QtCore.QRect(100, 260, 113, 25))
            self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: data2(self))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        if d[2]=="d":
            self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_2.setGeometry(QtCore.QRect(370, 260, 113, 25))
            self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 260, 67, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        for i in range(0,len(list_)):
            self.comboBox_2.setItemText(i+1, _translate("MainWindow", list_[i]))
        if self.d[2]=="d":
            self.label_2.setText(_translate("MainWindow", "Departure To"))
        else:
            self.label_2.setText(_translate("MainWindow", "Arriving From"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_4.setText(_translate("MainWindow", "Departure Time"))
        self.label_5.setText(_translate("MainWindow", "Arriving Time"))
        if self.d[2] == "d":
            self.label.setText(_translate("MainWindow", "Economy"))
            self.label_6.setText(_translate("MainWindow", "Business"))
            self.label_3.setText(_translate("MainWindow", "Ticket Cost(INR)"))

    def er(self,t):
        pass






if __name__ == "__main__":
    import sys
    list_ = ["jh","edjhehd","dewhde", "dgejg", "ehgdjuh"]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Add1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
