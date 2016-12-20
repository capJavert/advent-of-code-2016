from hashlib import md5
import os

directions = ["U", "D", "L", "R"]


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


def get_options(passcode):
    m = md5()
    m.update(passcode.encode())
    hash_string = m.hexdigest()
    open_directions = ["CLOSED"] * 4

    for i, c in enumerate(hash_string[0:4]):
        if c in "bcdef":
            open_directions[i] = "OPEN"
        else:
            open_directions[i] = "CLOSED"

    return open_directions


def check_locked(passcode):
    m = md5()
    m.update(passcode.encode())
    hash_string = m.hexdigest()

    for i, c in enumerate(hash_string[0:4]):
        if c in "bcdef":
            return False

    return True


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
    old_position = [1, 1]
    lock = False

    while True:
        os.system('clear')

        options = get_options(passcode+path)

        if lock:
            options[lock] = "CLOSED"
            lock = False
        else:
            old_position = my_position

        print_options(passcode+path)

        if options[0] == "OPEN" and maze[my_position[0]-1][my_position[1]] != "#" and not check_locked(passcode+path+"U"):
            path += "U"
            my_position[0] -= 2
        elif options[1] == "OPEN" and maze[my_position[0] + 1][my_position[1]] != "#" and not check_locked(passcode+path+"D"):
            path += "D"
            my_position[0] += 2
        elif options[2] == "OPEN" and maze[my_position[0]][my_position[1]-1] != "#" and not check_locked(passcode+path+"L"):
            path += "L"
            my_position[1] -= 2
        elif options[3] == "OPEN" and maze[my_position[0]][my_position[1]+1] != "#" and not check_locked(passcode+path+"R"):
            path += "R"
            my_position[1] += 2
        else:
            my_position = old_position
            lock = path[-1]
            path = path[:-1]
            lock = directions.index(lock)

        print_maze(my_position, maze)
        print("PATH:", path)
        print("------------------------------")

main()
