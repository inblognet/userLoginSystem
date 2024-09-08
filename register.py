import mysql

import database
import hashlib


def register_user(username, email, password):
    conn = database.connect()
    cursor = conn.cursor()

    # Hashing the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
        )
        conn.commit()
        print("User registered successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # Example user data for testing
    username = input("Enter a username: ")
    email = input("Enter an email: ")
    password = input("Enter a password: ")

    register_user(username, email, password)
