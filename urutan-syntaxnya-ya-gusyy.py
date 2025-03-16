# Data String gusyyyy 
name = "Mala Kurniawan"
gender = "Perempuan"
address = "Indonesia"
job = "Python Developer"

uppercase_name = name.upper()
lowercase_name = name.lower()
title_case_name = name.title()

stripped_address = address.strip()  # Menghapus spasi di awal dan akhir
substring_job = job[0:6]  # Mengambil substring dari indeks 0 sampai 5

replaced_gender = gender.replace("Perempuan", "Wanita")  # Mengganti substring

full_info = f"{name}, {gender}, {address}, {job}"

contains_python = "Python" in job  # Memeriksa keberadaan substring

formatted_string = f"Nama: {name}, Jenis Kelamin: {gender}, Alamat: {address}, Pekerjaan: {job}"

length_of_name = len(name)
length_of_address = len(address)

address_list = address.split(",")  # Memecah string berdasarkan koma

import re
pattern = r"\bMala\b"  # Mencari nama 'Mala'
match = re.search(pattern, name)

print("Hasil Manipulasi String:")
print("---------------------------------------------------")
print(f"| {'Operasi':<30} | {'Hasil':<50} |")
print("---------------------------------------------------")
print(f"| Mengubah Kasus Huruf:                  | {uppercase_name:<50} |")
print(f"| Mengubah Kasus Huruf (Lower):          | {lowercase_name:<50} |")
print(f"| Mengubah Kasus Huruf (Title Case):     | {title_case_name:<50} |")
print(f"| Memotong dan Mengambil Substring:       | {stripped_address:<50} |")
print(f"| Substring Pekerjaan:                    | {substring_job:<50} |")
print(f"| Mengganti Substring:                     | {replaced_gender:<50} |")
print(f"| Menggabungkan String:                   | {full_info:<50} |")
print(f"| Memeriksa Substring 'Python':           | {contains_python:<50} |")
print(f"| Format String:                          | {formatted_string:<50} |")
print(f"| Panjang Nama:                           | {length_of_name:<50} |")
print(f"| Panjang Alamat:                         | {length_of_address:<50} |")
print(f"| Alamat sebagai List:                    | {address_list:<50} |")
print(f"| Mencari 'Mala' dalam Nama:             | {'Ditemukan' if match else 'Tidak Ditemukan':<50} |")
print("---------------------------------------------------")
