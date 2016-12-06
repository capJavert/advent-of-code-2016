import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/9FAXzEqD")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def main():
    data_strings = get_and_prepare_data_string()

    message = ""
    message_length = len(data_strings[0])
    letters = "abcdefghijklmnopqrstuvwxyz"
    position_counts = []

    for i in range(0, message_length):
        letter_count = {}

        for l in letters:
            letter_count[l] = 0

        position_counts.append(letter_count)

    for string in data_strings:
        for (index, letter) in enumerate(string):
            position_counts[index][letter] += 1

    for count in position_counts:
        message += min(count, key=lambda p: count[p])

    print(message)

main()
