
class Disc:
    def __init__(self, i, n, position):
        self.id = i
        self.n = n
        self.position = position

    def rotate(self, time):
        position = self.position + time
        position %= self.n

        return position


def main():
    data_strings = [
        "Disc  # 1 has 13 positions; at time=0, it is at position 11.",
        "Disc  # 2 has 5 positions; at time=0, it is at position 0.",
        "Disc  # 3 has 17 positions; at time=0, it is at position 11.",
        "Disc  # 4 has 3 positions; at time=0, it is at position 0.",
        "Disc  # 5 has 7 positions; at time=0, it is at position 2.",
        "Disc  # 6 has 19 positions; at time=0, it is at position 17.",
        "Disc  # 7 has 11 positions; at time=0, it is at position 0."
    ]

    time = 0
    discs = []

    for string in data_strings:
        disc = [int(s) for s in string.replace(".", "").split(" ") if s.isdigit()]
        discs.append(Disc(disc[0], disc[1], disc[2]))

    aligned = False

    while not aligned:
        aligned = True
        t_time = time

        for disc in discs:
            t_time += 1
            if disc.rotate(t_time) != 0:
                aligned = False
                break

        if aligned:
            print(time)
        else:
            time += 1

main()
