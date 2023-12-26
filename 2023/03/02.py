import fileinput
import itertools


def get_adjacent_asterisk(schema, x, y):
    d = [-1, 0, 1]
    for x0, y0 in itertools.product(d, d):
        x1 = x + x0
        y1 = y + y0
        if x0 == 0 and y0 == 0:
            continue
        elif x1 >= len(schema) or y1 >= len(schema[0]) or x1 < 0 or y1 < 0:
            continue
        else:
            s = schema[x1][y1]
            if s == "*":
                return x1, y1
    return None, None


if __name__ == "__main__":
    schema = [l for l in fileinput.input()]
    res = 0
    history = []
    
    for x, row in enumerate(schema):
        num = ""
        ast_x, ast_y = None, None
        for y, char in enumerate(row):
            if char.isnumeric():
                num += char
                if ast_x is None:
                    ast_x, ast_y = get_adjacent_asterisk(schema, x, y)
            elif num and ast_x is not None:
                num = int(num)
                if history:
                    other = [num for num, x0, y0 in history if x0 == ast_x and y0 == ast_y]
                    if other:
                        res += other[0] * num
                    else:
                        history.append((num, ast_x, ast_y))
                else:
                    history.append((num, ast_x, ast_y))
                num = ""
                ast_x, ast_y = None, None
            else:
                num = ""

    print(res)
 