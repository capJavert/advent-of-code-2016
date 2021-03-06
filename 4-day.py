import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/Gt6FNrqN")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def gidfs(string):
    """
    get id from string
    :param string:
    :return:
    """
    return int(string.split("[")[0].split("-")[-1])


def prepare_data():
    data = get_and_prepare_data_string()

    return data


def is_real_room(string):
    letters = sorted(list("".join(string.split("[")[0].split("-")[:-1])))

    checksum = string.split("[")[1].replace("]", "")

    letter_counts = {}

    for letter in letters:
        letter_counts[letter] = letters.count(letter)

    my_checksum = ""
    for (key, value) in sorted(letter_counts.items(), key=lambda x: (-x[1], x[0])):
        my_checksum += key

    return True if my_checksum[0:5] == checksum else False


def decode_name(string, shift):
    decoded_name = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    encoded_name = " ".join(string.split("[")[0].split("-")[:-1])

    for x in encoded_name:
        if letters.find(x) >= 0:
            decoded_name += letters[(letters.find(x)+shift) % len(letters)]
        else:
            decoded_name += " "

    return decoded_name


def main():
    data_strings = get_and_prepare_data_string()

    for string in data_strings:
        if is_real_room(string):
            print(decode_name(string, gidfs(string)), gidfs(string))

main()
