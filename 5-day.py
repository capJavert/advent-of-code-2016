from hashlib import md5


def main():
    password = ""
    door_id = "abbhdwsy"
    index = 0

    while len(password) < 8:
        m = md5()
        string = door_id+str(index)
        m.update(string.encode())
        hash_string = m.hexdigest()
        
        if hash_string[0:5] == "00000":
            password += hash_string[5]

        index += 1

    print(password)

main()
