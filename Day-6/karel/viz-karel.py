def visualize_karel_world(positions, beeper_counts):
    world = []
    for pos, count in zip(positions, beeper_counts):
        if count > 0:
            world.append("B")
        else:
            world.append("-")

    print("Posisi: ", " ".join(map(str, positions)))
    print("Beeper: ", " ".join(world))

positions = list(range(1, 11))
beeper_counts = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

visualize_karel_world(positions, beeper_counts)
