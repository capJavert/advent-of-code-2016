import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/0pCiwLE0")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def main():
    data_strings = get_and_prepare_data_string()

    file = ""

    for string in data_strings:
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
                a_char = string[index:index+a]
                b = int(marker.split("x")[-1])

                for i in range(0, b):
                    file += a_char

                marker = ""
                marker_mode = False
                index += a
                continue

            if marker_mode:
                marker += char
            else:
                file += char

            index += 1

    print(len(file.replace(" ", "")))

main()
