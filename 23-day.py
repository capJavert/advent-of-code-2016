import requests

registers = {"a": 7, "b": 0, "c": 0, "d": 0}
overload = []


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/Pbwcm6Ha")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def cpy(value, register):
    try:
        if value.replace("-", "").isnumeric():
            registers[register] = int(value)
        else:
            registers[register] = registers[value]
    except:
        return -1


def inc(register):
    try:
        registers[register] += 1
    except:
        return -1


def dec(register):
    try:
        registers[register] -= 1
    except:
        return -1


def jnz(x, goto):
    try:
        if not x.replace("-", "").isnumeric():
            x = registers[x]

        if not goto.replace("-", "").isnumeric():
            goto = registers[goto]

        if x != 0:
            return int(goto)
        else:
            return 1
    except:
        return 1


def tgl(index, x, commands):
    try:
        if not x.isnumeric():
            x = registers[x]

        if x != 0:
            x = int(x) + index
            command = commands[x]

            if "inc" in command:
                commands[x] = commands[x].replace("inc", "dec")
            elif "dec" in command or "tgl" in command:
                commands[x] = commands[x].replace(commands[x][:3], "inc")
            elif "jnz" in command:
                commands[x] = commands[x].replace("jnz", "cpy")
            elif "cpy" in command:
                commands[x] = commands[x].replace("cpy", "jnz")

        return commands
    except:
        return commands


def main():
    data_strings = get_and_prepare_data_string()
    """data_strings = [
        "cpy 2 a",
        "tgl a",
        "tgl a",
        "tgl a",
        "cpy 1 a",
        "dec a",
        "dec a"
    ]"""

    index = 0
    while index < len(data_strings):
        command = data_strings[index]
        next_index = 1

        if "cpy" in command:
            cpy(command.split(" ")[1], command.split(" ")[2])

        if "inc" in command:
            inc(command.split(" ")[1])

        if "dec" in command:
            dec(command.split(" ")[1])

        if "tgl" in command:
            x = command[-1]
            data_strings = tgl(index, x, data_strings)

        if "jnz" in command:
            next_index = jnz(command.split(" ")[1], command.split(" ")[2])

        index += next_index

    print("A:", registers["a"], "B:", registers["b"], "C:", registers["c"], "D:", registers["d"])

main()
