import requests


class Instruction:
    def __init__(self, low_type, low, high_type, high):
        self.low = low
        self.high = high
        self.low_type = low_type
        self.high_type = high_type

class Bot:
    def __init__(self, index):
        self.id = index
        self.low = None
        self.high = None
        self.instructions = []

    @staticmethod
    def gto(oid, value):
        output_bin[oid] = value

    @staticmethod
    def gtb(bot, value):
        bots.setdefault(bot, Bot(bot))

        bots[bot].set_value(value)

    def execute(self):
        if self.low and self.high:
            instruction = self.instructions[0]
            self.instructions.pop(0)

            if instruction.low_type == "bot":
                self.gtb(instruction.low, self.low)
                self.low = None
            else:
                self.gto(instruction.low, self.low)
                self.low = None

            if instruction.high_type == "bot":
                self.gtb(instruction.high, self.high)
                self.high = None
            else:
                self.gto(instruction.high, self.high)
                self.high = None

    def set_value(self, value):
        if not value:
            return 0

        target_bots[self.id].append(value)

        if not self.low and not self.high:
            self.low = value
        else:
            if value > self.low:
                self.high = value
            else:
                old = self.low
                self.low = value
                self.high = old

output_bin = {}
bots = {}
target_bots = []

for i in range(0, 300):
    target_bots.append([])


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin, string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/HjZxJFzT")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def output(value, oid):
    output_bin[oid] = value


def goes(value, bot):
    bots.setdefault(bot, Bot(bot))

    bots[bot].set_value(value)


def main():
    data_strings = get_and_prepare_data_string()

    for index, string in enumerate(data_strings):
        if "goes" in string:
            instructions = [int(s) for s in string.split() if s.isdigit()]

            bot = instructions[1]
            value = instructions[0]
            goes(value, bot)

        if "gives" in string:
            instructions = [int(s) for s in string.split() if s.isdigit()]

            bots.setdefault(instructions[0], Bot(instructions[0]))

            if "low to bot" in string and "high to bot" in string:
                bots[instructions[0]].instructions.append(Instruction(
                    "bot",
                    instructions[1],
                    "bot",
                    instructions[2]
                ))
            if "low to output" in string and "high to output" in string:
                bots[instructions[0]].instructions.append(Instruction(
                    "output",
                    instructions[1],
                    "output",
                    instructions[2]
                ))
            if "low to bot" in string and "high to output" in string:
                bots[instructions[0]].instructions.append(Instruction(
                    "bot",
                    instructions[1],
                    "output",
                    instructions[2]
                ))
            if "low to output" in string and "high to bot" in string:
                bots[instructions[0]].instructions.append(Instruction(
                    "output",
                    instructions[1],
                    "bot",
                    instructions[2]
                ))

    bots_have_instructions = True

    while bots_have_instructions:
        bots_have_instructions = False

        for key, bot in bots.items():
            if len(bot.instructions):
                bots_have_instructions = True
                bot.execute()

    for index, bot in enumerate(target_bots):
        value_one = False
        value_two = False

        for value in bot:
            if value == 17:
                value_one = True

            if value == 61:
                value_two = True

        if value_one and value_two:
            print(index)
            break


main()
