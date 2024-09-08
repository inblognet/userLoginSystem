import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # default MySQL user, replace with your username if needed
        password="",  # enter your MySQL password, if set
        database="user_system"
    )
