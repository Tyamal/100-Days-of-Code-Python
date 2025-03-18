import random

def baca_data_kepegawaian(nama_file):
    with open(nama_file, 'r') as file:
        data = file.readlines()
    return [line.strip().split(', ') for line in data]

def hitung_masa_pensiun(umur):
    usia_pensiun = 55
    return usia_pensiun - umur

def pilih_karyawan(data):
    karyawan_valid = []
    for karyawan in data:
        id_karyawan, nama, alamat, gaji, umur, lama_bekerja, posisi = karyawan
        umur = int(umur)
        lama_bekerja = int(lama_bekerja)
        gaji = int(gaji)
        
        masa_pensiun = hitung_masa_pensiun(umur)
        
        if masa_pensiun > 0:
            karyawan_valid.append(karyawan)

    jabatan_urut = {
        'Manager': 1,
        'Supervisor': 2,
        'Staff': 3
    }
    
    karyawan_valid.sort(key=lambda x: (jabatan_urut[x[6]], -int(x[3]), -int(x[5])))

    return karyawan_valid

data_kepegawaian = baca_data_kepegawaian('data_kepegawaian.txt')
karyawan_terpilih = pilih_karyawan(data_kepegawaian)

if karyawan_terpilih:
    karyawan_acak = random.choice(karyawan_terpilih)
    print("Karyawan yang dipilih secara acak berdasarkan kriteria adalah:")
    print(f"ID: {karyawan_acak[0]}, Nama: {karyawan_acak[1]}, Alamat: {karyawan_acak[2]}, Gaji: {karyawan_acak[3]}, Umur: {karyawan_acak[4]}, Lama Bekerja: {karyawan_acak[5]}, Posisi: {karyawan_acak[6]}")
else:
    print("Tidak ada karyawan yang memenuhi kriteria.")
