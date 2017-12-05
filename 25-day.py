import requests
import signal as sig
import threading

import time

from multiprocessing import Manager, Value, Process

#registers = {"a": 101, "b": 0, "c": 0, "d": 0}


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/WjmjVn2L")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def cpy(value, register, registers):
    try:
        if value.replace("-", "").isnumeric():
            registers[register] = int(value)
        else:
            registers[register] = registers[value]
    except:
        pass

    return registers


def inc(register, registers):
    try:
        registers[register] += 1
    except:
        pass

    return registers


def dec(register, registers):
    try:
        registers[register] -= 1
    except:
        pass

    return registers


def jnz(x, goto, registers):
    try:
        if x == "0" and goto == "0":
            return 1

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


def tgl(index, x, commands, registers):
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


def out(x, registers, signal):
    if not x.replace("-", "").isnumeric():
        x = registers[x]

    signal.append(x)

    # print(x)
    return signal


def main(a, name):
    global NEXT
    data_strings = get_and_prepare_data_string()
    index = 0

    while True:
        signal = []
        registers = {"a": a.value, "b": 0, "c": 0, "d": 0}

        while len(signal) < 40:
            command = data_strings[index]
            next_index = 1

            if "cpy" in command:
                registers = cpy(command.split(" ")[1], command.split(" ")[2], registers)

            if "inc" in command:
                registers = inc(command.split(" ")[1], registers)

            if "dec" in command:
                registers = dec(command.split(" ")[1], registers)

            if "out" in command:
                signal = out(command.split(" ")[1], registers, signal)

            if "tgl" in command:
                x = command[-1]
                data_strings = tgl(index, x, data_strings, registers)

            if "jnz" in command:
                next_index = jnz(command.split(" ")[1], command.split(" ")[2], registers)

            index += next_index

        #print("Thread"+str(name))
        print(a)
        #print(signal[:20])

        if signal[:20] == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
            print("done")
            break

        a.value += 1


manager = Manager()
av = manager.Value('a', 1)

for i in range(20):
    process = Process(target=main, args=[av, i])
    process.start()
    time.sleep(1)
