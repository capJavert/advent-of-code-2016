import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    data_strings = []
    request = requests.get("http://pastebin.com/raw/tfRrctp5")
    request.encoding = 'ISO-8859-1'

    triangle_data = request.text.replace("\n", " ").split()

    for j in range(0, 3):
        strings_part = []
        for i in range(0, len(triangle_data), 3):
            strings_part.append(triangle_data[j+i])

        data_strings += strings_part

    column_data_strings = []
    for i in range(0, len(data_strings), 3):
        column_data_strings.append([data_strings[i], data_strings[i+1], data_strings[i+2]])

    return column_data_strings


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
