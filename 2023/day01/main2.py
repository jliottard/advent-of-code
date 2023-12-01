import sys

digit_name_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
def parse_digit(string: str, start_index: int) -> tuple[str, int]:
    # from the start_index, try to parse the beginning of the string to find a
    # digit
    # return: the found digit if parse is sucessful and the number of
    # characters parsed
    c = 0
    for i in range(start_index, len(string)):
        c += 1
        for name in digit_name_to_digit.keys():
            if len(name) > len(string) - (i + 1):
                continue
            if string[start_index:i+len(name)] == name:
                return str(digit_name_to_digit[name]), c
    return None, 1

if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        val_sum = 0
        for line in input_file:
            first_digit = None
            last_digit = None
            i = 0
            while i < len(line) - 1:
                char = line[i]
                if not char.isdigit():
                    maybe_parsed_digit, parsed_len = parse_digit(line, i)
                    if maybe_parsed_digit is not None:
                        if first_digit is None:
                            first_digit = maybe_parsed_digit
                        last_digit = maybe_parsed_digit
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    last_digit = char
                i += 1
            val_sum += int(first_digit + last_digit)
        print(val_sum)

