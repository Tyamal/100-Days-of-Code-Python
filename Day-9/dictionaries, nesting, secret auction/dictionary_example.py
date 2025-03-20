# dictionary_example.py

def main():
    # Membuat dictionary
    phone_book = {
        "Alice": "123-456-7890",
        "Bob": "987-654-3210",
        "Charlie": "555-555-5555"
    }

    # Menambahkan entri baru
    phone_book["David"] = "444-444-4444"

    # Menghapus entri
    del phone_book["Alice"]

    # Mencetak semua entri
    for name, number in phone_book.items():
        print(f"{name}: {number}")

if __name__ == "__main__":
    main()
