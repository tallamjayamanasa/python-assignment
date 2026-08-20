import mysql.connectors

connection = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="student_db"
    )

    if connection.is_connected():
        print("Database connected successfully.")

except mysql.connector.Error as e:
    print("Database error:", e)

finally:
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")