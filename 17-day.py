from hashlib import md5

directions = ["UP", "DOWN", "LEFT", "RIGHT"]


def print_maze(position, maze):
    for index, line in enumerate(maze):
        string = ""

        for j, item in enumerate(line):
            if [index, j] == position:
                string += "S"
            else:
                string += item

        print(string)


def print_options(passcode):
    m = md5()
    m.update(passcode.encode())
    hash_string = m.hexdigest()

    for i, c in enumerate(hash_string[0:4]):
        if c in "bcdef":
            print(directions[i]+":", "OPEN")
        else:
            print(directions[i] + ":", "CLOSED")


def main():
    maze = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", "|", " ", "|", " ", "|", " ", "#"],
        ["#", "-", "#", "-", "#", "-", "#", "-", "#"],
        ["#", " ", "|", " ", "|", " ", "|", " ", "#"],
        ["#", "-", "#", "-", "#", "-", "#", "-", "#"],
        ["#", " ", "|", " ", "|", " ", "|", " ", "#"],
        ["#", "-", "#", "-", "#", "-", "#", "-", "#"],
        ["#", " ", "|", " ", "|", " ", "|"],
        ["#", "#", "#", "#", "#", "#", "#", " ", "V"]
    ]

#   name = input("What is your name? ")
    name = "javert"
    passcode = "pgflpeqp"
    path = ""
    my_position = [1, 1]

    print_maze(my_position, maze)
    print_options(passcode + path)
    print("---------------------------------")

    command = None
    while command != "done":
        command = input(name+"@bunnyquarters:~$ ")

        if "up" in command:
            path += "U"
            my_position[0] -= 2

        if "down" in command:
            path += "D"
            my_position[0] += 2

        if "left" in command:
            path += "L"
            my_position[1] -= 2

        if "right" in command:
            path += "R"
            my_position[1] += 2

        if "#" in command:
            path = path[:-1]

        print_options(passcode+path)
        print_maze(my_position, maze)
        print("PATH:", path)

    print("---------------------------------")
    print("FINAL PATH:", path)

main()
