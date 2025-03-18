def move_karel(steps):
    for _ in range(steps):
        move()

def collect_beeper():
    while beepers_present():
        pick_beeper()

def arrange_beepers():
    while front_is_clear():
        collect_beeper()
        move_karel(1)
    collect_beeper()  # Mengumpulkan beeper terakhir jika ada

def place_beepers(count):
    for _ in range(count):
        put_beeper()

def main():
    # Karel mulai di posisi awal
    arrange_beepers()  # Kumpulkan semua beeper
    move_karel(1)  # Bergerak satu langkah ke depan
    place_beepers(5)  # Tempatkan 5 beeper di posisi baru

# Jalankan fungsi utama
main()
