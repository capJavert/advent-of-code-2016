import requests


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


def main():
    grid = []
    position = [0, 26]
    data_strings = get_and_prepare_data_string()

    for string in data_strings:
        grid.append(string.split())

    print_grid(grid, position)
main()
