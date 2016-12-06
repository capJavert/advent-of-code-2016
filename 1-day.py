
def get_vectors_from_string(data_string):
    return data_string.split(", ")


def calc_distance(vectors):
    orientation = 0
    distance = 0

    locations = []
    x = 0
    y = 0

    for vector in vectors:
        old_orientation = orientation
        if old_orientation < 0:
            old_orientation += 360

        for i in range(0, int(vector[1:4])):
            if old_orientation == 0:
                if vector[0] == "L":
                    x -= 1
                else:
                    x += 1

            if old_orientation == 90:
                if vector[0] == "L":
                    y += 1
                else:
                    y -= 1

            if old_orientation == 180:
                if vector[0] == "L":
                    x += 1
                else:
                    x -= 1

            if old_orientation == 270:
                if vector[0] == "L":
                    y -= 1
                else:
                    y += 1

            for location in locations:
                if location == [x, y]:
                    print("HIT!", [x, y])
                    return abs(x)+abs(y)

            locations.append([x, y])

        if vector[0] == "L":
            orientation -= 90
        else:
            orientation += 90

        orientation %= 360

    return abs(x)+abs(y)


def main():
    data_string = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2"
    #data_string = "R8, R4, R4, R8"

    vectors = get_vectors_from_string(data_string)

    print(calc_distance(vectors))

main()
