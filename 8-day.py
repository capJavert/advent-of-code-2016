import requests
import numpy

width = 50
height = 6


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/nYHYEYEW")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def passcode_to_string(passcode):
    string = ""

    for row in passcode:
        row_string = ""
        for e in row:
            row_string += e

        string += (row_string+"\n")

    return string


def rect(command, passcode):
    command = command.split("rect ")[-1]
    a = int(command.split("x")[0])
    b = int(command.split("x")[1])

    for i in range(0, b):
        for j in range(0, a):
            passcode[i][j] = "#"

    return passcode


def rotate_row(command, passcode):
    command = command.split("rotate row y=")[-1]
    a = int(command.split(" by")[0])
    b = int(command.split("by ")[-1])

    passcode[a] = numpy.roll(passcode[a], b)

    return passcode

def rotate_column(command, passcode):
    command = command.split("rotate column x=")[-1]
    a = int(command.split(" by")[0])
    b = int(command.split("by ")[-1])

    column = []

    for i in range(0, height):
        column.append(passcode[i][a])

    column = numpy.roll(column, b)

    for i in range(0, height):
        passcode[i][a] = column[i]

    return passcode


def main():
    data_strings = get_and_prepare_data_string()

    passcode = []

    for i in range(0, height):
        data = []

        for j in range(0, width):
            data.append(".")

        passcode.append(data)

    for string in data_strings:
        if "rect" in string:
            passcode = rect(string, passcode)

        if "rotate row" in string:
            passcode = rotate_row(string, passcode)

        if "rotate column" in string:
            passcode = rotate_column(string, passcode)

    print(passcode_to_string(passcode))

main()
