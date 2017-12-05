import requests


class Node:
    def __init__(self, identifier, size, used, avail, use):
        self.id = identifier
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
    for i in range(0, 27):
        for j in range(0, 37):
            if grid["/dev/grid/node-x"+str(j)+"-y"+str(i)].use == 0 and [j, i] != position:
                print("_", " ", end="")
            elif not is_viable("/dev/grid/node-x"+str(j)+"-y"+str(i)) and [j, i] != position:
                print("#", " ", end="")
            elif [j, i] == position:
                print("G", " ", end="")
            else:
                print(".", " ", end="")

        print()


def get_viable_pairs(grid):
    global pairs
    global viable_nodes
    pairs = []
    viable_nodes = {}

    for id_a, node_a in grid.items():
        for id_b, node_b in grid.items():
            if id_a != id_b and 0 < node_a.used <= node_b.avail:
                pairs.append((id_a, id_b))
                viable_nodes[id_a], viable_nodes[id_b] = True, True

                
    return grid


def nodes_viable(node_a_id, node_b_id):
    global pairs

    return (node_a_id, node_b_id) in pairs


def is_viable(node_id):
    global viable_nodes

    return node_id in viable_nodes


def move_data(grid, node_a_id, node_b_id):
    global pairs

    if nodes_viable(node_a_id, node_b_id):
        grid[node_b_id].used += grid[node_a_id].used
        grid[node_b_id].avail -= grid[node_a_id].used
        grid[node_a_id].used, grid[node_a_id].avail = 0, grid[node_a_id].size

    grid = get_viable_pairs(grid)

    return grid


pairs = []
viable_nodes = {}


def get_maze(grid):
    global pairs
    maze = []

    return maze


def main():
    global pairs
    grid = {}
    position = [36, 0]
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

        grid[node.id] = node

    grid = get_viable_pairs(grid)
    print(len(pairs))

    print_grid(grid, position)


main()
