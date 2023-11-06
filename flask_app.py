import pyrebase
from flask import Flask
from PyQt5 import QtWidgets, QtCore
import sys


# Configure application
app = Flask(__name__)

# Your Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCjZmikoyD4-JoobcZlEWA-UL7kwbhJY_E",
    "authDomain": "selamat-c7b68.firebaseapp.com",
    "projectId": "selamat-c7b68",
    "databaseURL": "https://selamat-c7b68-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "selamat-c7b68.appspot.com",
    "messagingSenderId": "569379372374",
    "appId": "1:569379372374:web:efc500e2cca83d0d3f6af7",
    "measurementId": "G-NP6DD0SNE0",
}

# Configure app to use Google Firebase Realtime Database
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()


def fetch_data():
    try:
        # Fetch data from your Firebase database (replace with your data path)
        data_accident = database.child("Accident").get().val()
        data_ev = database.child("Emergency Vehicle").get().val()
        if data_accident is not None and data_ev is not None:
            return {"data_accident": data_accident, "data_ev": data_ev}
        else:
            print("No data fetched from the database.")
            return {"data_accident": {}, "data_ev": {}}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"data_accident": {}, "data_ev": {}}


# Updated populate_data function to populate both tables
def populate_data(data_accident, data_ev, ui):
    accident_table = ui.AccidentTable
    ev_table = ui.EVTable

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
    app.run(debug=True)
