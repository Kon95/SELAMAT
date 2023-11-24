import sys
from ui import Ui_Dialog
import data
import flask_app
from PyQt5 import QtCore, QtGui, QtWidgets, QtCore
import qdarktheme

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
        self.ui.alert2.clicked.connect(self.onCLick)
        self.alertTotal = 0
        self.updateGraph()

        self.showMaximized()
        self.setTimerGraph()
        self.setTimerTable()

    def setTimerGraph(self):
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.updateGraph)
        self.timer1.start(2000)

    def updateGraph(self):
        data.plot1()
        data.plot2()
        self.ui.traffic_img.setPixmap(QtGui.QPixmap("./assets/traffic_graph.png"))
        self.ui.crash_img.setPixmap(QtGui.QPixmap("./assets/accident_graph.png"))

    def setTimerTable(self):
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.updateTable)
        self.timer2.start(500)

    def updateTable(self):
        data_dict = flask_app.fetch_data()
        data_accident = data_dict.get("data_accident", {})
        data_ev = data_dict.get("data_ev", {})
        self.populate_data(data_accident, data_ev)
    
    def onCLick(self):
        self.alertTotal += 1
        if self.alertTotal %3 == 0:
            self.changeAlert("./assets/green.png")
        elif self.alertTotal %3 == 1:
            self.changeAlert("./assets/yellow.png")
        else:
            self.changeAlert("./assets/red.png")
        
    def changeAlert(self,path):
        self.ui.alert1.setPixmap(QtGui.QPixmap(path))
        self.ui.alert2.setPixmap(QtGui.QPixmap(path))

    def populate_data(self,data_accident, data_ev):
        accident_table = self.ui.accident_table
        ev_table = self.ui.ev_table

        # Clear any existing data
        accident_table.setRowCount(0)
        ev_table.setRowCount(0)

        if not data_accident or not data_ev:
            return  

        # Check and populate the AccidentTable with Accident data
        if isinstance(data_accident, dict):
            for key, value in data_accident.items():
                if isinstance(value, dict):
                    row_position = accident_table.rowCount()
                    accident_table.insertRow(row_position)
                    accident_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(key))
                    accident_table.setItem(
                        row_position, 1, QtWidgets.QTableWidgetItem(value.get("Code", ""))
                    )
                    accident_table.setItem(
                        row_position,
                        2,
                        QtWidgets.QTableWidgetItem(value.get("Location", "")),
                    )
                    accident_table.setItem(
                        row_position, 3, QtWidgets.QTableWidgetItem(value.get("Time", ""))
                    )
                    accident_table.setItem(
                        row_position,
                        4,
                        QtWidgets.QTableWidgetItem(value.get("Severity", "")),
                    )
        else:
            print("Invalid data format for Accident data:", data_accident)

        # Check and populate the EVTable with Emergency Vehicle data
        if isinstance(data_ev, dict):
            for key, value in data_ev.items():
                if isinstance(value, dict):
                    row_position = ev_table.rowCount()
                    ev_table.insertRow(row_position)
                    ev_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(key))
                    ev_table.setItem(
                        row_position, 1, QtWidgets.QTableWidgetItem(value.get("Code", ""))
                    )
                    ev_table.setItem(
                        row_position,
                        2,
                        QtWidgets.QTableWidgetItem(value.get("EV_Allocated", "")),
                    )
                    ev_table.setItem(
                        row_position, 3, QtWidgets.QTableWidgetItem(value.get("EV_TOA", ""))
                    )
        else:
            print("Invalid data format for Emergency Vehicle data:", data_ev)



if __name__ == "__main__":
    qdarktheme.enable_hi_dpi()
    app = QtWidgets.QApplication(sys.argv)    
    qdarktheme.setup_theme()

    ui = Main()
    ui.show()
    sys.exit(app.exec_())