import sys
if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        val_sum = 0
        for line in input_file:
            first_digit = 0
            last_digit = 0
            for char in line:
                if char.isdigit() and first_digit == 0:
                    first_digit = char
                if char.isdigit():
                    last_digit = char
            val_sum += int(first_digit + last_digit)
        print(val_sum)

