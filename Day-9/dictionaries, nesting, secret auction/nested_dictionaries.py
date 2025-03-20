# nested_dictionaries.py

def main():
    # Membuat nested dictionary
    students = {
        "student1": {
            "name": "Alice",
            "age": 20,
            "grades": [85, 90, 88]
        },
        "student2": {
            "name": "Bob",
            "age": 22,
            "grades": [78, 82, 80]
        }
    }

    # Menambahkan data untuk student3
    students["student3"] = {
        "name": "Charlie",
        "age": 21,
        "grades": [92, 95, 94]
    }

    # Mencetak informasi setiap siswa
    for student_id, info in students.items():
        print(f"{student_id}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

if __name__ == "__main__":
    main()
