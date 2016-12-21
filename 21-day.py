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
    password = "fbgdceah"

    data_strings.reverse()

    for operation in data_strings:
        if "swap position" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            params.reverse()
            temp = list(password)
            s = temp[params[1]]
            temp[params[1]] = temp[params[0]]
            temp[params[0]] = s
            password = "".join(temp)
        elif "swap letter" in operation:
            params = operation.split(" ")
            params = [params[2], params[-1]]
            params.reverse()
            password = password.replace(params[0], "#").replace(params[1], params[0]).replace("#", params[1])
        elif "reverse" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            temp = password[params[0]:params[1]+1]
            temp = temp[::-1]
            password = password[:params[0]] + temp + password[params[1]+1:]
        elif "rotate" in operation and "step" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            temp = deque(password)
            if "right" in operation:
                temp.rotate(-params[0])
            else:
                temp.rotate(params[0])
            password = "".join(temp)
        elif "move" in operation:
            params = [int(x) for x in operation.split() if x.isnumeric()]
            params.reverse()
            temp = list(password)
            char = temp[params[0]]
            temp.pop(params[0])
            temp.insert(params[1], char)
            password = "".join(temp)
        elif "rotate based":
            params = [operation[-1]]
            index = password.find(params[0])
            temp = deque(password)

            if index == 0 or index == 1:
                temp.rotate(-1)
            elif index == 2:
                temp.rotate(2)
            elif index == 3:
                temp.rotate(-2)
            elif index == 4:
                temp.rotate(1)
            elif index == 5:
                temp.rotate(-3)
            elif index == 7:
                temp.rotate(4)

            password = "".join(temp)

    print(password)
main()
