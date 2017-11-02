from hashlib import md5
from heapq import heappop, heappush

directions = ["UP", "DOWN", "LEFT", "RIGHT"]


def translate_orientation(path):
    path = path.replace("S", "D")
    path = path.replace("N", "U")
    path = path.replace("E", "R")
    path = path.replace("W", "L")

    return path


def print_maze(maze, position):
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            if [i, j] == position:
                print(5, " ", end="")
            else:
                print(c, " ", end="")

        print()


def adjust_with_options(path, position):
    global passcode

    original_maze = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]

    new_maze = list(original_maze)

    m = md5()
    path = translate_orientation(path)

    m.update((passcode+path).encode())
    hash_string = m.hexdigest()

    for i, c in enumerate(hash_string[0:4]):
        if c in "bcdef":
            if directions[i] == "UP" and new_maze[position[0] - 1][position[1]] != "#":
                new_maze[position[0] - 1][position[1]] = " "
            elif directions[i] == "DOWN" and new_maze[position[0] + 1][position[1]] != "#":
                new_maze[position[0] + 1][position[1]] = " "
            elif directions[i] == "LEFT" and new_maze[position[0]][position[1] - 1] != "#":
                new_maze[position[0]][position[1] - 1] = " "
            elif directions[i] == "RIGHT" and new_maze[position[0]][position[1] + 1] != "#":
                new_maze[position[0]][position[1] + 1] = " "
        else:
            if directions[i] == "UP":
                new_maze[position[0] - 1][position[1]] = "#"
            elif directions[i] == "DOWN":
                new_maze[position[0] + 1][position[1]] = "#"
            elif directions[i] == "LEFT":
                new_maze[position[0]][position[1] - 1] = "#"
            elif directions[i] == "RIGHT":
                new_maze[position[0]][position[1] + 1] = "#"

    int_maze = []

    for i, line in enumerate(new_maze):
        int_maze.append([])

        for j, c in enumerate(line):
            int_maze[i].append(1 if (c == "#" or c == "-" or c == "|") else 0)

    # print(path)
    # print_maze(int_maze, position)

    return int_maze


def maze2graph(current_maze):
    height = len(current_maze)
    width = len(current_maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not current_maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not current_maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not current_maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def find_path_astar(maze):
    global last_state
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    pr_queue = []
    heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))
    fix = False
    _, cost, path, current = (None, None, None, None)

    while True:
        while pr_queue:
            visited = set()
            if not fix:
                _, cost, path, current = heappop(pr_queue)
            else:
                fix = False

            last_state = _, cost, path, current
            graph = maze2graph(adjust_with_options(path, [current[0], current[1]]))
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in graph[current]:
                heappush(pr_queue, (cost + heuristic(neighbour, goal), cost + 1,
                                    path + direction, neighbour))

        _, cost, path, current = last_state
        fix = True


last_state = None
passcode = "pgflpeqp"


def main():
    original_maze = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]

    print(translate_orientation(find_path_astar(original_maze)))


main()
