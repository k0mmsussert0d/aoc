import fileinput
import itertools


def get_adjacent_symbols(schema, x, y):
    d = [-1, 0, 1]
    res = []
    for x0, y0 in itertools.product(d, d):
        x1 = x + x0
        y1 = y + y0
        if x0 == 0 and y0 == 0:
            continue
        elif x1 >= len(schema) or y1 >= len(schema[0]) or x1 < 0 or y1 < 0:
            continue
        else:
            s = schema[x1][y1]
            if s != "\n" and s != "." and not s.isnumeric():
                res.append(s)
    return res


if __name__ == "__main__":
    schema = [l for l in fileinput.input()]
    
    sum = 0
    for x, row in enumerate(schema):
        num = ""
        candidate = False
        for y, char in enumerate(row):
            if char.isnumeric():
                num += (char)
                if not candidate and get_adjacent_symbols(schema, x, y):
                    candidate = True
            elif num:
                if candidate:
                    sum += int(num)
                num = ""
                candidate = False
    print(sum)
