def cek_tunjangan(usia, jabatan, status_keanggotaan):
    if usia < 0:
        return "Usia tidak valid."
    
    if jabatan.lower() == 'manager':
        if status_keanggotaan.lower() == 'ya':
            return "Anda mendapatkan tunjangan kesehatan dan tunjangan transportasi."
        else:
            return "Anda mendapatkan tunjangan transportasi."
    elif jabatan.lower() == 'staff':
        if usia > 30 and status_keanggotaan.lower() == 'ya':
            return "Anda mendapatkan tunjangan kesehatan."
        else:
            return "Anda tidak mendapatkan tunjangan."
    elif jabatan.lower() == 'intern':
        return "Anda tidak mendapatkan tunjangan."
    else:
        return "Jabatan tidak dikenali."

data_karyawan = [
    {"nama": "Andi", "usia": 35, "jabatan": "Manager", "status_keanggotaan": "ya"},
    {"nama": "Budi", "usia": 28, "jabatan": "Staff", "status_keanggotaan": "tidak"},
    {"nama": "Cindy", "usia": 32, "jabatan": "Staff", "status_keanggotaan": "ya"},
    {"nama": "Doni", "usia": 22, "jabatan": "Intern", "status_keanggotaan": "tidak"},
    {"nama": "Eka", "usia": 40, "jabatan": "Manager", "status_keanggotaan": "ya"},
    {"nama": "Fani", "usia": 29, "jabatan": "Staff", "status_keanggotaan": "tidak"},
    {"nama": "Gina", "usia": 31, "jabatan": "Staff", "status_keanggotaan": "ya"},
    {"nama": "Hadi", "usia": 45, "jabatan": "Manager", "status_keanggotaan": "tidak"},
    {"nama": "Ika", "usia": 27, "jabatan": "Intern", "status_keanggotaan": "tidak"},
    {"nama": "Joko", "usia": 33, "jabatan": "Staff", "status_keanggotaan": "ya"},
    {"nama": "Kiki", "usia": 38, "jabatan": "Manager", "status_keanggotaan": "ya"},
    {"nama": "Lina", "usia": 24, "jabatan": "Intern", "status_keanggotaan": "tidak"},
    {"nama": "Maya", "usia": 30, "jabatan": "Staff", "status_keanggotaan": "ya"},
    {"nama": "Nina", "usia": 26, "jabatan": "Staff", "status_keanggotaan": "tidak"},
    {"nama": "Omar", "usia": 50, "jabatan": "Manager", "status_keanggotaan": "ya"},
    {"nama": "Pia", "usia": 29, "jabatan": "Staff", "status_keanggotaan": "tidak"},
    {"nama": "Qori", "usia": 21, "jabatan": "Intern", "status_keanggotaan": "tidak"},
    {"nama": "Rudi", "usia": 34, "jabatan": "Staff", "status_keanggotaan": "ya"},
    {"nama": "Sari", "usia": 36, "jabatan": "Manager", "status_keanggotaan": "tidak"},
    {"nama": "Tina", "usia": 23, "jabatan": "Intern", "status_keanggotaan": "ya"},
    {"nama": "Udin", "usia": 31, "jabatan": "Staff", "status_keanggotaan": "ya"},
]

for karyawan in data_karyawan:
    nama = karyawan["nama"]
    usia = karyawan["usia"]
    jabatan = karyawan["jabatan"]
    status_keanggotaan = karyawan["status_keanggotaan"]

    hasil = cek_tunjangan(usia, jabatan, status_keanggotaan)
    print(f"Hasil untuk {nama}: {hasil}")
