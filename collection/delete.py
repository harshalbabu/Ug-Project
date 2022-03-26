# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot


class delete1(object):
    def setupUi(self, mainWindow, data, data4,to_home):
        self.data4 = data4
        self.data =data
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1246, 428)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1221, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        print(len(data))
        self.tableWidget.setRowCount(len(data))
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Uroob")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 370, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:to_home())
        


        
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    @pyqtSlot()
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            if currentQTableWidgetItem.column() == 11:
                r = currentQTableWidgetItem.row()
                pk = self.data[r][0]
                print(pk)
                self.data4(pk)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Delete Flight"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Trip_no"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Airlines"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Flight No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "From"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "To"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("mainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("mainWindow", "cost(eco)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("mainWindow", "cost(bus)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("mainWindow", "delay"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("mainWindow", "cancel"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("mainWindow", "Passanger list"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        for d,i in zip(self.data,range(len(self.data))):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("mainWindow", str(d[0])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i,1, item)
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("mainWindow", str(d[2])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i,2, item)
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("mainWindow", str(d[1])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 3, item)
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("mainWindow", str(d[3])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 4, item)
            item = self.tableWidget.item(i, 4)
            item.setText(_translate("mainWindow", str(d[5])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 5, item)
            item = self.tableWidget.item(i, 5)
            item.setText(_translate("mainWindow", str(d[4])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 6, item)
            item = self.tableWidget.item(i, 6)
            item.setText(_translate("mainWindow", str(d[6])))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 7, item)
            if d[3]=="CCJ":
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, 7, item)
                item.setText(_translate("mainWindow", str(d[7])))
                item = self.tableWidget.item(i, 7)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, 8, item)
                item.setText(_translate("mainWindow", str(d[8])))
                item = self.tableWidget.item(i, 8)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Ubuntu Mono")
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 11, item)
            item = self.tableWidget.item(i, 11)
            item.setText(_translate("mainWindow", "Delete"))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 9, item)
            item.setText(_translate("mainWindow", str(d[9])))
            item = self.tableWidget.item(i, 9)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 10, item)
            item.setText(_translate("mainWindow", str(d[10])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.clicked.connect(lambda :self.on_click())
        self.pushButton.setText(_translate("mainWindow", "Go Home"))
