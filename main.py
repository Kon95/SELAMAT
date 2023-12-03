import sys
from ui import Ui_Dialog
import data
import flask_app
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarktheme
import datetime
import time

LOCATION = "PETALING JAYA"

class Main(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.traffic_img.setPixmap(QtGui.QPixmap("./assets/traffic_graph.png"))
        self.ui.traffic_img.setScaledContent = True
        self.ui.crash_img.setPixmap(QtGui.QPixmap("./assets/accident_graph.png"))
        self.ui.crash_img.setScaledContent = True
        self.changeAlert("./assets/green.png")
        self.ui.alert1.clicked.connect(self.onCLick)
        self.ui.SystemName.clicked.connect(self.startVideo)
        self.ui.accident_table.verticalHeader().setVisible(False)
        self.ui.ev_table.verticalHeader().setVisible(False)
        self.step = 0

        self.alertTotal = 0
        self.updateGraph()

        self.showMaximized()

    def updateGraph(self):
        data.plot3()
        img1 = QtGui.QPixmap("./assets/traffic_graph.png").scaled(600,500,QtCore.Qt.KeepAspectRatio)
        img2 = QtGui.QPixmap("./assets/accident_graph.png").scaled(600,500,QtCore.Qt.KeepAspectRatio)
        self.ui.traffic_img.setPixmap(img1)
        self.ui.crash_img.setPixmap(img2)

    def keyPressEvent(self, event):
        if self.step%4==0:
                data = {
                    "Time": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    "Location": LOCATION,
                    "Severity": "Medium"
                }
                self.updateTable(1,data)
                self.ui.alert_text1.setText("Accident Detected")
                self.onCLick()
        elif self.step%4==1:
                data = {
                    "Time": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    "Location": LOCATION,
                    "Vehicle Detected": "Ambulance"
                }
                self.updateTable(2,data)
                self.ui.alert_text1.setText("Ambulance Detected")
                self.onCLick()
        elif self.step%4==2:
                data = {
                    "Time": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    "Location": LOCATION,
                    "Vehicle Detected": "Police"
                }
                self.updateTable(2,data)
                self.ui.alert_text1.setText("Police Detected")
        elif self.step%4==3:
                # self.resetTable()
                self.ui.alert_text1.setText("Clear")
                self.onCLick()
        self.step += 1
    
    def startVideo(self):
        data1 = {
            "Time": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            "Location": LOCATION,
            "Severity": "Medium"
        }

        data2 = {
            "Time": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            "Location": LOCATION,
            "Vehicle Detected": "Ambulance"
        }
        
        data3 = {
            "Time": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            "Location": LOCATION,
            "Vehicle Detected": "Police"
        }

        self.updateTable(1,data1)

    def updateTable(self, ind, data):
        if ind == 1:
            self.addItemInTable(self.ui.accident_table,data)
        else:
            self.addItemInTable(self.ui.ev_table,data)
    
    def resetTable(self):
        self.ui.accident_table.setRowCount(0)
        self.ui.ev_table.setRowCount(0)
    
    def onCLick(self):
        self.alertTotal += 1
        if self.alertTotal %3 == 0:
            self.changeAlert("./assets/green.png")
        elif self.alertTotal %3 == 2:
            self.changeAlert("./assets/yellow.png")
        else:
            self.changeAlert("./assets/red.png")
        
    def changeAlert(self,path):
        self.ui.alert1.setPixmap(QtGui.QPixmap(path))

    def addItemInTable(self, table, dic):
        pos = table.rowCount()
        table.insertRow(pos)
        for i, value in enumerate(dic.values()):
            table.setItem(pos, i, QtWidgets.QTableWidgetItem(value))


if __name__ == "__main__":
    # qdarktheme.enable_hi_dpi()
    app = QtWidgets.QApplication(sys.argv)    
    qdarktheme.setup_theme()

    ui = Main()
    ui.show()
    sys.exit(app.exec_())