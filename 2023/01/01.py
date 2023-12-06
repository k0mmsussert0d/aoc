if __name__ == "__main__":
    with open("input_test", "r") as f:
        lines = f.readlines()

    res = 0
    for line in lines:
        digits = [s for s in line if s.isdigit()]
        res += int(digits[0] + digits[-1])
    
    print(res)
