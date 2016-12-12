import requests

registers = {"a": 0, "b": 0, "c": 1, "d": 0}


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/qj6mMDJh")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def cpy(value, register):
    if value.isnumeric():
        registers[register] = int(value)
    else:
        registers[register] = registers[value]


def inc(register):
    registers[register] += 1


def dec(register):
    registers[register] -= 1


def jnz(x, goto):
    if not x.isnumeric():
        x = registers[x]

    if x != 0:
        return int(goto)
    else:
        return 1


def main():
    data_strings = get_and_prepare_data_string()

    index = 0
    while index < len(data_strings):
        command = data_strings[index]

        if "cpy" in command:
            cpy(command.split(" ")[1], command.split(" ")[2])

        if "inc" in command:
            inc(command.split(" ")[1])

        if "dec" in command:
            dec(command.split(" ")[1])

        if "jnz" in command:
            index += jnz(command.split(" ")[1], command.split(" ")[2])
        else:
            index += 1

    print("A:", registers["a"], "B:", registers["b"], "C:", registers["c"], "D:", registers["d"])

main()
