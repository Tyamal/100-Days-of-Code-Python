def visualize_karel_world(positions, beeper_counts):
    # Membuat visualisasi dunia Karel
    world = []
    for pos, count in zip(positions, beeper_counts):
        if count > 0:
            world.append("B")  # B untuk beeper
        else:
            world.append("-")  # - untuk posisi kosong

    # Menampilkan visualisasi
    print("Posisi: ", " ".join(map(str, positions)))
    print("Beeper: ", " ".join(world))

# Data posisi dan jumlah beeper
positions = list(range(1, 11))
beeper_counts = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Menjalankan fungsi untuk visualisasi
visualize_karel_world(positions, beeper_counts)
