import requests


class Node:
    def __init__(self, name, size, used, avail, use):
        self.name = name
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/W93M5ybr")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def print_grid(grid, position):
    for i in range(0, len(grid), 27):
        string = ""
        for j in range(i, i+27):
            if int(grid[j][2].replace("T", "")) != 0:
                if [i, j] == position:
                    string += " G "
                elif i == 0 and j == 0:
                    string += "(.) "
                else:
                    string += " .  "
            else:
                if [i, j] == position:
                    string += " G "
                elif i == 0 and j == 0:
                    string += "(_) "
                else:
                    string += " _  "

        print(string)


def get_viable_pairs(grid):
    pairs = []

    for node_a in grid:
        for node_b in grid:
            if node_a.name != node_b.name and 0 < node_a.used <= node_b.avail:
                pairs.append((node_a.name, node_b.name))

    return pairs


def main():
    grid = []
    position = [0, 26]
    data_strings = get_and_prepare_data_string()

    for string in data_strings:
        raw_node = string.split()
        node = Node(
                raw_node[0],
                int(raw_node[1].replace("T", "")),
                int(raw_node[2].replace("T", "")),
                int(raw_node[3].replace("T", "")),
                int(raw_node[4].replace("%", ""))
            )

        grid.append(node)

    pairs = get_viable_pairs(grid)
    print(len(pairs))


main()
