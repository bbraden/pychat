from dbtools import *
from datetime import datetime

time = datetime.now().strftime("%X")
date = datetime.now().strftime("%x")
while True:
    m = input('msg: ')

    if m == 'end':
        m = 'test.py ended'
        ms = {"message": m, "date": date, "time": time}
        db.insert_one(ms)
        break

    ms = {"message": m, "date": date, "time": time}
    db.insert_one(ms)