import mysql

import database
import hashlib


def login_user(username, password):
    conn = database.connect()
    cursor = conn.cursor()

    # Hashing the password to compare with stored hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                       (username, hashed_password))
        user = cursor.fetchone()
        if user:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # Example login
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    login_user(username, password)
