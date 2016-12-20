import time

bn = 3014387


def slow_main():
    """
    part 1 implementation
    part 2 would be more slow and more ugly :) check main_slow2() function for this
    :return:
    """
    n = 3014387
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


def slow_main2(no):
    n = no
    elves = []

    for i in range(0, n):
        elves.append(i + 1)

    i = int(n / 2)
    while len(elves) != 1:
        if n == 1:
            break

        elves.pop(i)
        n = len(elves)

        if n % 2 == 0:
            i += 1

        i %= n

    print(elves[0])


def main(no):
    w = 1

    for i in range(1, no):
        w = w % i + 1

        if w > (i + 1) / 2:
            w += 1

    print(w)

start_time = time.time()
main(bn)
print("--- %s seconds ---" % (time.time() - start_time))

"""
SLOW IMPLEMENTATION, PART 1 RUNS FOR OVER 1h 30m on my 2.9GHz i5
ONLY HERE TO SHOW HOW MY ALGORITHM SOLUTION IS (PAPER AND PEN BEFORE MAC AND KEYBOARD!!)
start_time = time.time()
slow_main()
print("--- %s seconds ---" % (time.time() - start_time))
"""
