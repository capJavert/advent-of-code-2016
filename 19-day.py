import time

n = 3014387


def slow_main():
    global n
    elf = 0
    elves = [1] * n
    lap = False

    while True:
        if elves[elf] != 0:
            l_elf = elf + 1
            if l_elf >= n:
                l_elf %= 1

            while True:
                if elves[l_elf] != 0:
                    elves[elf] += elves[l_elf]
                    elves[l_elf] = 0
                    break

                l_elf += 1

                if l_elf >= n:
                    l_elf %= n

            if n in elves:
                break

        if not lap:
            elf += 2
        else:
            elf += 1

        if elf >= n:
            elf %= n

        if elf == 0:
            lap = True

    print(elf+1)


def main():
    global n
    elves = []

    for i in range(0, n):
        elves.append(i+1)

    while len(elves) != 1:
        temp_elves = []
        for i in range(0, n, 2):
            temp_elves.append(elves[i])

        if n % 2 != 0:
            temp_elves.pop(0)

        elves = temp_elves
        n = len(elves)

    print(elves[0])


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

"""
SLOW IMPLEMENTATION RUNS FOR OVER 1h 30m on my 2.9GHz i5
ONLY HERE TO SHOW HOW MY ALGORITHM SOLUTION IS (PAPER AND PEN BEFORE MAC AND KEYBOARD!!)
start_time = time.time()
slow_main()
print("--- %s seconds ---" % (time.time() - start_time))
"""
