import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    data_strings = []
    request = requests.get("http://pastebin.com/raw/tfRrctp5")
    request.encoding = 'ISO-8859-1'

    for line in request.text.splitlines():
        line = ' '.join(line.split())

        data_strings.append(line.split(" "))

    return data_strings


def is_valid_triangle(triangle):
    return True if \
        (int(triangle[0]) + int(triangle[1]) > int(triangle[2])) and \
        (int(triangle[1]) + int(triangle[2]) > int(triangle[0])) and \
        (int(triangle[0]) + int(triangle[2]) > int(triangle[1])) \
        else False


def main():
    data_strings = get_and_prepare_data_string()
    valid_triangles = 0

    for triangle in data_strings:
        valid_triangles = valid_triangles + 1 if is_valid_triangle(triangle) else valid_triangles

    print(valid_triangles)

main()
