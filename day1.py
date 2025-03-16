# Mendeklarasikan variabel
name = "Mala"  # Nama pengguna
age = 25           # Usia pengguna
height = 1.65     # Tinggi pengguna dalam meter
is_student = True  # Apakah pengguna seorang pelajar

# Menghitung tahun lahir
current_year = 2023
birth_year = current_year - age

# Mencetak informasi pengguna
print("Nama:", name)
print("Usia:", age)
print("Tinggi:", height, "meter")
print("Apakah pelajar:", is_student)
print("Tahun lahir:", birth_year)

# Menggunakan variabel dalam kalimat
if is_student:
    print(name, "adalah seorang pelajar.")
else:
    print(name, "bukan seorang pelajar.")
