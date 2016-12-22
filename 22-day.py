import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/W93M5ybr")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def main():
    discs = []
    data_strings = get_and_prepare_data_string()

    for string in data_strings:
        disc = string.split()

        if int(disc[2].replace("T", "")) != 0:
            for string2 in data_strings:
                disc2 = string2.split()

                if disc2 != disc and int(disc[2].replace("T", "")) <= int(disc2[3].replace("T", "")):
                    discs.append([disc, disc2])

    print("PAIRS:", len(discs))
main()
