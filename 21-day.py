import requests
from collections import deque


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/y6BC5itW")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def main():
    data_strings = get_and_prepare_data_string()
    password = "abcdefgh"
    """password = "decab"
    data_strings = [
        "swap position 4 with position 0",
        "swap letter d with letter b",
        "reverse positions 0 through 4",
        "rotate left 1 step",
        "move position 1 to position 4",
        "move position 3 to position 0",
        "rotate based on position of letter b",
        "rotate based on position of letter d"
    ]"""

    for operation in data_strings:
        if "swap position" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            temp = list(password)
            s = temp[params[1]]
            temp[params[1]] = temp[params[0]]
            temp[params[0]] = s
            password = "".join(temp)
        elif "swap letter" in operation:
            params = operation.split(" ")
            params = [params[2], params[-1]]
            password = password.replace(params[0], "#").replace(params[1], params[0]).replace("#", params[1])
        elif "reverse" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            temp = password[params[0]:params[1]+1]
            temp = temp[::-1]
            password = password[:params[0]] + temp + password[params[1]+1:]
        elif "rotate" in operation and "step" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            temp = deque(password)
            if "left" in operation:
                temp.rotate(-params[0])
            else:
                temp.rotate(params[0])
            password = "".join(temp)
        elif "move" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            temp = list(password)
            char = temp[params[0]]
            temp.pop(params[0])
            temp.insert(params[1], char)
            password = "".join(temp)
        elif "rotate based":
            params = [operation[-1]]
            index = password.find(params[0])
            index = index + 1 if index >= 4 else index
            temp = deque(password)
            temp.rotate(index + 1)
            password = "".join(temp)

    print(password)
main()
