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
        id_karyawan,
