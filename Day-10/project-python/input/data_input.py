import sqlite3

def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data_pemerintah (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            jabatan TEXT NOT NULL,
            instansi TEXT NOT NULL
        )
    ''')
    conn.commit()

def insert_data(conn, nama, jabatan, instansi):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO data_pemerintah (nama, jabatan, instansi)
        VALUES (?, ?, ?)
    ''', (nama, jabatan, instansi))
    conn.commit()

def close_db(conn):
    conn.close()
