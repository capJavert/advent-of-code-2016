import itertools
import requests
from heapq import heappop, heappush


def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def find_path_astar(maze, start, goal):
    # start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    pr_queue = []
    heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))
    visited = set()
    graph = maze2graph(maze)
    # print(graph)
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        # print(str(current) + ", ")
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue, (cost + heuristic(neighbour, goal), cost + 1,
                                path + direction, neighbour))
    return "NO WAY!"


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("https://pastebin.com/raw/mdCtuwYF")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def main():
    data_strings = get_and_prepare_data_string()
    maze = []
    waypoints = {}

    for i, line in enumerate(data_strings):
        maze.append([])

        for j, c in enumerate(line):
            maze[i].append(1 if c == "#" else 0)

            if c.isdigit():
                waypoints[c] = (i, j)

    paths = itertools.permutations(waypoints)
    min_steps = 100000000

    for path in paths:
        print(path)
        steps = 0
        start = waypoints["0"]

        for waypoint in path:
            if waypoint == "0":
                continue

            goal = waypoints[waypoint]
            steps += len(find_path_astar(maze, start, goal))

            start = goal

        if steps < min_steps:
            min_steps = steps
            print(min_steps)

    print("MIN STEPS: " + min_steps)


main()
