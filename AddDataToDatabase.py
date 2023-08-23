import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL':"https://attendacemanagement-faea8-default-rtdb.firebaseio.com/"})


ref = db.reference('Students')

data = {
    "18101":
        {
            "name": "Jai Gangwar",
            "major": "Electrical",
            "start_year": 2018,
            "total_attendance": 6,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2023-08-22 00:54:34"
        },
    "19101":
        {
            "name": "Pinkee Kumari Singh",
            "major": "Computer",
            "start_year": 2019,
            "total_attendance": 5,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-08-20 00:54:58"
        }

}
for key, value in data.items():
    ref.child(key).set(value)
