
def main():
    last_row = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^......."
    safe_count = 0
    new_row = ""

    for i in range(0, 400000):
        safe_count += last_row.count(".")

        for j, c in enumerate(last_row):
            left = "." if j == 0 else last_row[j-1]
            right = "." if j == len(last_row)-1 else last_row[j+1]
            center = last_row[j]

            if left == "^" and center == "^" and right == ".":
                new_row += "^"
            elif center == "^" and right == "^" and left == ".":
                new_row += "^"
            elif left == "^" and center == "." and right == ".":
                new_row += "^"
            elif left == "." and center == "." and right == "^":
                new_row += "^"
            else:
                new_row += "."

        last_row = new_row
        new_row = ""

    print("SAFE TILES:", safe_count)

main()
