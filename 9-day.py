import requests

file_size = 0


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/0pCiwLE0")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def decompress(string):
    global file_size
    file = ""
    marker = ""
    marker_mode = False
    index = 0
    while index < len(string):
        char = string[index]

        if char == "(":
            marker_mode = True
            index += 1
            continue

        if char == ")":
            index += 1
            a = int(marker.split("x")[0])
            a_char = string[index:index + a]
            b = int(marker.split("x")[-1])

            for i in range(0, b):
                decompress(a_char)

            marker = ""
            marker_mode = False

            index += a
            continue

        if marker_mode:
            marker += char
        else:
            file += char

        index += 1

    file_size += len(file)


def main():
    global file_size
    data_strings = get_and_prepare_data_string()

    for i, string in enumerate(data_strings):
        string = string.replace(" ", "")
        decompress(string)

    print(file_size)

main()
