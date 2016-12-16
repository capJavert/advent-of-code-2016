
def print_maze(maze):
    for index, line in enumerate(maze):
        string = ""

        for item in line:
            string += item

        print(string)


def main():
    a = "10001001100000001"
    disk_size = 35651584
    checksum = ""

    while len(a) < disk_size:
        b = a
        b = b[::-1]
        b = b.replace("0", "X").replace("1", "0").replace("X", "1")
        a = a + "0" + b

    a = a[0:disk_size]

    while len(checksum) % 2 == 0:
        checksum = ""
        for i in range(0, len(a), 2):
            if a[i:i+2] == "00" or a[i:i+2] == "11":
                checksum += "1"
            else:
                checksum += "0"

        a = checksum

    print("CHECKSUM:", checksum)

main()
