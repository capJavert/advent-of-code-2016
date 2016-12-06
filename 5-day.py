from hashlib import md5


def is_numeric(string):
    try:
        int(string)
    except:
        return False

    return True


def main():
    password_size = 0
    password = ["_", "_", "_", "_", "_", "_", "_", "_"]
    door_id = "abbhdwsy"
    index = 0

    while password_size < 8:
        m = md5()
        string = door_id+str(index)
        m.update(string.encode())
        hash_string = m.hexdigest()

        if hash_string[0:5] == "00000" and is_numeric(hash_string[5]):
            if 8 > int(hash_string[5]) >= 0 and password[int(hash_string[5])] == "_":
                password_size += 1
                password[int(hash_string[5])] = str(hash_string[6])

        index += 1

    print("".join(password))

main()
