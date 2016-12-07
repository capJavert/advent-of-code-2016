import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/Fgqt9gaZ")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def is_abba(string):
    if string != len(string) * string[0] and len(string) == 4:
        return True if str(string) == str(string)[::-1] else False
    else:
        return False


def main():
    data_strings = get_and_prepare_data_string()

    valid_ips = 0

    for string in data_strings:
        is_valid = False
        is_valid_hypernet = True
        invert = False

        for (index, letter) in enumerate(string):
            if letter == "[":
                invert = True
                continue

            if letter == "]":
                invert = False
                continue

            if is_abba(string[index:index+4]) and not invert:
                is_valid = True

            if is_abba(string[index:index+4]) and invert:
                is_valid_hypernet = False

        if is_valid and is_valid_hypernet:
            valid_ips += 1

    print(valid_ips)

main()
