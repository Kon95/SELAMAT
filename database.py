import pyrebase

# Firebase configuration
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

data_accident = {
    "Code": "ABC",
    "Location": "Petaling Jaya",
    "Number": "1",
    "Severity": "Very severe",
    "Time": "12:34pm",
}

data_ev = {
    "Code": "ABC",
    "Number": "1",
    "Severity": "Very severe",
    "EV_Allocated": "Ambulance",
    "EV_TOA": "12:34pm",
}

database.child("Accident").push(data_accident)
database.child("Emergency Vehicle").push(data_ev)
