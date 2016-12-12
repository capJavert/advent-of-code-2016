import requests

floors = []
floor = 0
items = ["/", "/"]
steps = 0


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin triangle string was just to big to insert inside this code :)
    """
    request = requests.get("http://pastebin.com/raw/jCtzh3E9")
    request.encoding = 'ISO-8859-1'

    return request.text.splitlines()


def is_fried():
    objects = floors[floor] + items

    for item in objects:
        if item == "/" or "M" not in item:
            continue

        match = item.split("M")[0]+"G"

        if match not in objects and len([obj for obj in objects if "G" in obj]):
            return True

    return False


def print_floors_map():
    for i in range(3, -1, -1):
        f = floors[i]

        if floor == i:
            string = "[E] F" + str(i) + " "
        else:
            string = "    F"+str(i)+" "

        for item in f:
            string += item+" "

        print(string)


def move(direction):
    global floor
    global steps

    floor = floor-1 if direction == "down" else floor+1

    if floor > 3:
        floor -= 1
        print("You are on the top floor!")
    elif floor < 0:
        floor += 1
        print("You are on the ground floor!")
    else:
        print_floors_map()
        steps += 1
        print("STEPS: ", steps)


def pick(item):
    if item in floors[floor]:
        if items[0] == "/":
            items[0] = item
        else:
            items[1] = item

        floors[floor].pop(floors[floor].index(item))
    else:
        print("Item is not on this floor!")


def drop(item):
    if item == "1" or item == "2":
        if items[int(item)-1]:
            floors[floor].append(items[int(item)-1])
            items[int(item)-1] = "/"
    else:
        print("You don't have that item!")


def inventory():
    print(items[0], items[1])


def main():
    data_strings = get_and_prepare_data_string()
    name = input("What is your name? ")

    for index, string in enumerate(data_strings):
        floor = string.split("contains a ")[-1].replace("and ", "").replace(",", "").replace(".", "").split(" a ")

        if floor[0] != "The fourth floor contains nothing relevant":
            for j, f in enumerate(floor):
                floor[j] = f.split(" ")[0][0:2].upper()+f.split(" ")[1][0].upper()

            floors.append(floor)
        else:
            floors.append([])

    command = None
    while command != "done":
        command = input(name+"@bunnyquarters:~$ ")

        if "mv" in command:
            move(command.split(" ")[-1])

        if "pick" in command:
            pick(command.split(" ")[-1])

        if "drop" in command:
            drop(command.split(" ")[-1])

        if "inv" in command:
            inventory()

        if "stat" in command:
            print_floors_map()

        if is_fried():
            print("*********************************")
            print("*********************************")
            print("*********************************")
            print("BUZZZZZZZZZZZZZZZZZZZZZZ!!!!")
            print("YOU ARE FRIED!!!!!")
            print("*********************************")
            print("*********************************")
            print("*********************************")
            command = "done"

    print("---------------------------------")
    print_floors_map()
    print("STEPS: ", steps)

main()
