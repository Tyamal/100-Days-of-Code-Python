import sqlite3

def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data_pemerintah')
    return cursor.fetchall()

def display_data(data):
    for row in data:
        print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Instansi: {row[3]}')

def close_db(conn):
    conn.close()
