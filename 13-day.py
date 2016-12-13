
def print_maze(maze):
    for index, line in enumerate(maze):
        string = ""

        for item in line:
            string += item

        print(string)


def main():
    maze_number = 1362
    maze = []

    for y in range(0, 40):
        maze.append([])
        for x in range(0, 40):
            cord_multiple = x*x + 3*x + 2*x*y + y + y*y
            cord_multiple += maze_number
            bin_string = str(bin(cord_multiple))[2:]

            if bin_string.count("1") % 2 == 0:
                maze[y].append(".")
            else:
                maze[y].append("#")

    print_maze(maze)

main()
