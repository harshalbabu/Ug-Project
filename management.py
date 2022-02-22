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
sqliteConnection = sqlite3.connect('db.sqlite3')
cursor = sqliteConnection.cursor()


def insert_flight_details(cursor):

    cursor.execute("SELECT MAX(trip_id) FROM booking_flight_details;")
    max = cursor.fetchone()[0]
    if max is None:
        max = 0
    print(max)
    f_id = input("enter flight id: ")
    f_name = input("enter flight name: ")
    f = input("from: ")
    to = input("to: ")
    c = f"insert into booking_flight_details values({max+1},{f_id},'{f_name}','{f}','{to}')"
    print(c)
    cursor.execute(c)
    return cursor

def show_passanger(cursor):
    cursor.execute("SELECT * FROM booking_flight_details;")
    data = cursor.fetchall()
    for d in data:
        print(f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]}")
    print()
    f = input("enter trip id >>> ")
    cursor.execute(f"SELECT * FROM booking_booking where trip_id = {f}")
    data = cursor.fetchall()
    print()
    for d in data:
        print(f"{d[0]} - {d[2]}")
    return cursor



choice = input("select choice : ")
if choice == '1':
    cursor = insert_flight_details(cursor)
elif choice == '2':
    show_passanger(cursor)
else:
    print("\ninvalied input\nExiting.....")
sqliteConnection.commit()
sqliteConnection.close()