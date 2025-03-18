# List of car data
cars = [
    {
        "id_mobil": 1,
        "nama_mobil": "Toyota Camry",
        "merek": "Toyota",
        "tahun_pembuatan": 2020,
        "harga": 350000000,  # dalam IDR
        "warna": "Hitam",
        "jenis_bahan_bakar": "Bensin"
    },
    {
        "id_mobil": 2,
        "nama_mobil": "Honda Civic",
        "merek": "Honda",
        "tahun_pembuatan": 2021,
        "harga": 400000000,
        "warna": "Putih",
        "jenis_bahan_bakar": "Bensin"
    },
    {
        "id_mobil": 3,
        "nama_mobil": "Suzuki Ertiga",
        "merek": "Suzuki",
        "tahun_pembuatan": 2019,
        "harga": 250000000,
        "warna": "Merah",
        "jenis_bahan_bakar": "Bensin"
    },
    {
        "id_mobil": 4,
        "nama_mobil": "Daihatsu Xenia",
        "merek": "Daihatsu",
        "tahun_pembuatan": 2020,
        "harga": 230000000,
        "warna": "Biru",
        "jenis_bahan_bakar": "Bensin"
    },
    {
        "id_mobil": 5,
        "nama_mobil": "Nissan Leaf",
        "merek": "Nissan",
        "tahun_pembuatan": 2022,
        "harga": 600000000,
        "warna": "Hijau",
        "jenis_bahan_bakar": "Listrik"
    }
]

# Print the car data
for car in cars:
    print(f"ID Mobil: {car['id_mobil']}")
    print(f"Nama Mobil: {car['nama_mobil']}")
    print(f"Merek: {car['merek']}")
    print(f"Tahun Pembuatan: {car['tahun_pembuatan']}")
    print(f"Harga: {car['harga']} IDR")
    print(f"Warna: {car['warna']}")
    print(f"Jenis Bahan Bakar: {car['jenis_bahan_bakar']}")
    print("-" * 40)
