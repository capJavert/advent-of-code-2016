import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/Fgqt9gaZ")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def is_aba(string):
    if string != len(string) * string[0] and len(string) == 3:
        return True if str(string) == str(string)[::-1] else False
    else:
        return False


def is_bab(string, aba):
    if string != len(string) * string[0] and len(string) == 3:
        return True if string == aba[1]+aba[0]+aba[1] else False
    else:
        return False


def main():
    data_strings = get_and_prepare_data_string()

    valid_super_strings = []
    valid_ips = 0

    for string in data_strings:
        invert = False
        aba_strings = []

        for (index, letter) in enumerate(string):
            if letter == "[":
                invert = True
                continue

            if letter == "]":
                invert = False
                continue

            if not invert:
                if is_aba(string[index:index+3]):
                    aba_strings.append(string[index:index+3])

        if len(aba_strings) > 0:
            valid_super_strings.append([string, aba_strings])

    for string in valid_super_strings:
        is_valid_hypernet = False
        invert = False

        for(index, letter) in enumerate(string[0]):
            if letter == "[":
                invert = True
                continue

            if letter == "]":
                invert = False
                continue

            if invert:
                for aba in string[1]:
                    if is_bab(string[0][index:index+3], aba):
                        is_valid_hypernet = True
                        break

            if is_valid_hypernet:
                valid_ips += 1
                break

    print(valid_ips)

main()
