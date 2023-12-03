# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v2_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1005, 689)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SystemName = ClickableLabel(Dialog)
        self.SystemName.setAlignment(QtCore.Qt.AlignCenter)
        self.SystemName.setObjectName("SystemName")
        self.verticalLayout_3.addWidget(self.SystemName)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.alert1 = ClickableLabel(Dialog)
        self.alert1.setText("")
        self.alert1.setPixmap(QtGui.QPixmap("green.png"))
        self.alert1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.alert1.setObjectName("alert1")
        self.horizontalLayout_2.addWidget(self.alert1)
        self.alert_text1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alert_text1.setFont(font)
        self.alert_text1.setObjectName("alert_text1")
        self.horizontalLayout_2.addWidget(self.alert_text1)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.accident_title = QtWidgets.QLabel(Dialog)
        self.accident_title.setObjectName("accident_title")
        self.verticalLayout.addWidget(self.accident_title)
        self.accident_table = QtWidgets.QTableWidget(Dialog)
        self.accident_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.accident_table.setRowCount(0)
        self.accident_table.setColumnCount(3)
        self.accident_table.setObjectName("accident_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.accident_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.accident_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.accident_table.setHorizontalHeaderItem(2, item)
        self.accident_table.horizontalHeader().setVisible(True)
        self.accident_table.horizontalHeader().setCascadingSectionResizes(False)
        self.accident_table.horizontalHeader().setDefaultSectionSize(200)
        self.accident_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.accident_table)
        self.ev_title = QtWidgets.QLabel(Dialog)
        self.ev_title.setObjectName("ev_title")
        self.verticalLayout.addWidget(self.ev_title)
        self.ev_table = QtWidgets.QTableWidget(Dialog)
        self.ev_table.setEnabled(True)
        self.ev_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ev_table.setObjectName("ev_table")
        self.ev_table.setColumnCount(3)
        self.ev_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ev_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ev_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ev_table.setHorizontalHeaderItem(2, item)
        self.ev_table.horizontalHeader().setVisible(True)
        self.ev_table.horizontalHeader().setCascadingSectionResizes(False)
        self.ev_table.horizontalHeader().setDefaultSectionSize(200)
        self.ev_table.horizontalHeader().setSortIndicatorShown(False)
        self.ev_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.ev_table)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.traffic_img = QtWidgets.QLabel(Dialog)
        self.traffic_img.setAlignment(QtCore.Qt.AlignCenter)
        self.traffic_img.setObjectName("traffic_img")
        self.verticalLayout_2.addWidget(self.traffic_img)
        self.crash_img = QtWidgets.QLabel(Dialog)
        self.crash_img.setAlignment(QtCore.Qt.AlignCenter)
        self.crash_img.setObjectName("crash_img")
        self.verticalLayout_2.addWidget(self.crash_img)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 10)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SystemName.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">SELAMAT</span></p></body></html>"))
        self.alert_text1.setText(_translate("Dialog", "<html><head/><body><p>Clear</p></body></html>"))
        self.accident_title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Accident</span></p></body></html>"))
        item = self.accident_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Time"))
        item = self.accident_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Location"))
        item = self.accident_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Severity"))
        self.ev_title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Emergency Vehicle</span></p></body></html>"))
        item = self.ev_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Time"))
        item = self.ev_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Location"))
        item = self.ev_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Vehicle Detected"))
        self.traffic_img.setText(_translate("Dialog", "Image"))
        self.crash_img.setText(_translate("Dialog", "Image"))
from clickablelabel import ClickableLabel
