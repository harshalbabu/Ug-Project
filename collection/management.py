"""
sqliteConnection.close()
cursor.fetchall()
cursor.execute(c)
sqliteConnection.commit()
c = "insert into booking_flight_details values(1,123,'abc',1324,'cochi','dubai')"
cursor = sqliteConnection.cursor()
sqliteConnection = sqlite3.connect('db.sqlite3')
import sqlite3
"""
import sqlite3
from datetime import datetime
sqliteConnection = sqlite3.connect('db.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = sqliteConnection.cursor()


def insert_flight_details(cursor,f_id,f_name,d,t,f_time,t_time,cost_b,cost_e):
    cursor.execute("SELECT MAX(trip_id) FROM booking_flight_details;")
    max = cursor.fetchone()[0]
    if max is None:
        max = 1000
    print(max)
    if t=="a":
        f = d
        to = "CCJ"
    else:
        to = d
        f = "CCJ"
    c = f"insert into booking_flight_details values({max+1},{f_id},'{f_name}','{f}','{to}','{f_time}','{t_time}',{cost_e},{cost_b},0,0)"
    print(c)
    cursor.execute(c)
    return cursor

def show_flight(cursor):
    cursor.execute("SELECT * FROM booking_flight_details;")
    data = cursor.fetchall()
    return data

def delete(cursor,f):
    cursor.execute(f"DELETE FROM booking_flight_details where trip_id = {f}")

def cancel(cursor,f):
    cursor.execute(f"UPDATE booking_flight_details set cancellation=1 where trip_id = {f}")

def delay(cursor,f,t):
    cursor.execute(f"UPDATE booking_flight_details set delay={t} where trip_id = {f}")

def u_cost(cursor,f,e,b):
    if e != "":
        cursor.execute(f"UPDATE booking_flight_details set cost_e={e} where trip_id = {f}")
    if b != "":
        cursor.execute(f"UPDATE booking_flight_details set cost_b={b} where trip_id = {f}")

def show_passanger(cursor, f):
    cursor.execute(f"SELECT * FROM booking_booking where trip_id = {f}")
    data = cursor.fetchall()
    return data

