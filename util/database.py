import sqlite3

conn = sqlite3.connect("reviews.db",check_same_thread=False)
cursor = conn.cursor()


def all_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")

    result = cursor.fetchall()
    cursor.close()
    return result

def all_reviews():
    pass

def register(username, password):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password)  VALUES ({username},{password});")
    cursor.close()

