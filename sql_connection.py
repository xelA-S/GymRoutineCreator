import mysql.connector

__connector=None


def create_sql_connection():
    global __connector

    if __connector is None:

        __connector=mysql.connector.connect(
            user="root",
            password="password123",
            database="gym_app"
        )

    return __connector