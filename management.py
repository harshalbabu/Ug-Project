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
    id = input("enter id: ")
    f_id = input("enter flight id: ")
    f_name = input("enter flight name: ")
    t_id = input("enter travel id: ")
    f = input("from: ")
    to = input("to: ")
    c = f"insert into booking_flight_details values({id},{f_id},'{f_name}',{t_id},'{f}','{to}')"
    print(c)
    cursor.execute(c)
    return cursor


cursor = insert_flight_details(cursor)
sqliteConnection.commit()
sqliteConnection.close()