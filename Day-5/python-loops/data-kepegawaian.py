import sqlite3

def create_database():
    conn = sqlite3.connect('mala_golf.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        salary REAL NOT NULL,
        age INTEGER NOT NULL,
        address TEXT NOT NULL,
        years_of_service INTEGER NOT NULL,
        position TEXT NOT NULL,
        birthplace TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

def add_employee(name, salary, age, address, years_of_service, position, birthplace):
    conn = sqlite3.connect('mala_golf.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO Employee (name, salary, age, address, years_of_service, position, birthplace)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, salary, age, address, years_of_service, position, birthplace))
    
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlite3.connect('mala_golf.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Employee')
    employees = cursor.fetchall()
    
    conn.close()
    return employees

create_database()

employees_data = [
    ('Alice Smith', 60000, 30, 'Jl. Melati No. 10, Jakarta', 5, 'Manager', 'Bandung'),
    ('Bob Johnson', 45000, 28, 'Jl. Kenanga No. 5, Surabaya', 3, 'Golf Pro', 'Yogyakarta'),
    ('Charlie Brown', 30000, 25, 'Jl. Anggrek No. 20, Bandung', 2, 'Caddy', 'Jakarta'),
    ('Diana Prince', 55000, 32, 'Jl. Mawar No. 15, Bali', 6, 'Supervisor', 'Medan'),
    ('Ethan Hunt', 40000, 29, 'Jl. Cempaka No. 8, Makassar', 4, 'Caddy', 'Palembang')
]

for employee in employees_data:
    add_employee(*employee)

employees = fetch_employees()
for employee in employees:
    print(f"Nomor Pegawai: {employee[0]}")
    print(f"Nama Pegawai: {employee[1]}")
    print(f"Gaji: {employee[2]}")
    print(f"Umur: {employee[3]}")
    print(f"Alamat: {employee[4]}")
    print(f"Masa Kerja: {employee[5]} tahun")
    print(f"Jabatan: {employee[6]}")
    print(f"Asal Kelahiran: {employee[7]}")
    print("-" * 40)
