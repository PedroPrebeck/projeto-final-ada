import sqlite3


def create_connection():
    conn = sqlite3.connect("pets.db", check_same_thread=False)
    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS pets
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, peso REAL)"""
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_pet(conn, nome, idade, peso):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pets (nome, idade, peso) VALUES (?, ?, ?)", (nome, idade, peso)
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting pet: {e}")


def fetch_all_pets(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pets")
        pets = cursor.fetchall()
        return pets
    except sqlite3.Error as e:
        print(f"Error fetching pets: {e}")
        return []
