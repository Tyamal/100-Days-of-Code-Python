CREATE TABLE IF NOT EXISTS Mobil (
    id_mobil INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_mobil TEXT NOT NULL,
    merek TEXT NOT NULL,
    tahun_pembuatan INTEGER NOT NULL,
    harga REAL NOT NULL,
    warna TEXT NOT NULL,
    jenis_bahan_bakar TEXT NOT NULL
);
