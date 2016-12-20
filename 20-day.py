import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/wmVmpF8A")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def main():
    data_strings = get_and_prepare_data_string()
    limit = 4294967295
    low = 0
    high = 0

    firewall = [[], []]

    for string in data_strings:
        ip_range = [int(x) for x in string.split("-")]

        if ip_range[0] > ip_range[1]:
            s = ip_range[1]
            ip_range[1] = ip_range[0]
            ip_range[0] = s

        firewall[0].append(ip_range[0])
        firewall[1].append(ip_range[1])

    firewall[0] = sorted(firewall[0])
    firewall[1] = sorted(firewall[1])

    ip_count = 0
    for i in range(0, len(firewall[0])):
        if high > firewall[0][i] > low:
            ip_count += (firewall[1][i] - high)
        else:
            ip_count += (firewall[1][i] - firewall[0][i] + 1)

        high = firewall[1][i]
        low = firewall[0][i]

    print(limit - ip_count + 1)

main()
