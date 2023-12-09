#!/usr/bin/python3
import sys
if __name__ == "__main__":
    with open(sys.argv[1], "rt") as input_text:
        seeds = [int(x) for x in  next(iter(input_text)).split(":")[1].split(" ")[1:]]
        next(iter(input_text))
        mappings = input_text.read()[:-1].split("\n\n")
        translations = []
        for mapping in mappings:
            range_maps = []
            raw_ranges = mapping.split(":")[1].split("\n")[1:]
            for x_range in raw_ranges:
                trans = [int(x) for x in x_range.split(" ")]
                input_range = [trans[1], trans[1] + trans[2] - 1]
                range_maps.append((input_range, trans[0]-trans[1]))
            translations.append(range_maps)
        locations = []
        def in_bounds(left, val, right):
            return left <= val <= right
        for seed in seeds:
            val = seed
            for translation in translations:
                for x_range in translation:
                    if in_bounds(x_range[0][0], val, x_range[0][1]):
                        val += x_range[1]
                        break
                # one for one if not in ranges
            locations.append(val)
        print(min(locations))

