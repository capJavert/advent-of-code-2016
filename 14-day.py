from hashlib import md5
import time

hashes = {}


def print_maze(maze):
    for index, line in enumerate(maze):
        string = ""

        for item in line:
            string += item

        print(string)


def find_first_string(string):
    index = len(string)+1
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    for char in characters:
        findex = string.find(char+char+char)
        if findex != -1 and findex < index:
            index = findex

    if index != len(string)+1:
        return string[index]
    else:
        return -1


def stretch_hash(hash_string):
    source_hash = hash_string

    if source_hash not in hashes:
        for j in range(0, 2016):
            m = md5()
            string = hash_string
            m.update(string.encode())
            hash_string = m.hexdigest()

        hashes[source_hash] = hash_string
    else:
        hash_string = hashes[source_hash]

    return hash_string


def main():
    salt = "qzyelonm"
    keys = []
    index = -1

    while True:
        if len(keys) < 64:
            index += 1
        else:
            break

        m = md5()
        string = salt + str(index)
        m.update(string.encode())
        hash_string = m.hexdigest()

        hash_string = stretch_hash(hash_string)

        char = find_first_string(hash_string)
        if char != -1:
            for i in range(index+1, index+1001):
                m = md5()
                string = salt + str(i)
                m.update(string.encode())
                check_string = m.hexdigest()

                check_string = stretch_hash(check_string)

                if char+char+char+char+char in check_string:
                    keys.append(hash_string)
                    print(index, hash_string)
                    break

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
