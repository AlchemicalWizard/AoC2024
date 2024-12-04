
def parse_data(filename):
    file = open(filename)
    lines = file.readlines()
    return [x.replace("\n", "") for x in lines]


def test(input, expected):
    if (input != expected):
        raise Exception("Test failed, expected " +
                        str(expected) + " but received " + str(input))
    print("test passed")


def check_for_match(lines, x, y):
    testDirections = [[0, 1], [0, -1], [1, 0],
                      [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    matches = 0
    for testDirection in testDirections:
        if scan_line(lines, x, y, testDirection):
            matches += 1

    return matches


def check_for_match_v2(lines, x, y):
    xOffsets = [-1, 1]

    matches = 0
    for xOffset in xOffsets:
        if scan_line_v2(lines, x, y, xOffset):
            matches += 1

    return matches == 2


def scan_line(lines, x, y, direction):
    scanFor = ['S', 'A', 'M']
    for i in range(1, 4):
        yCheck = y+(direction[1]*i)
        xCheck = x+(direction[0]*i)

        if (yCheck > len(lines)-1 or
            yCheck < 0 or
            xCheck > len(lines[yCheck])-1 or
                xCheck < 0):
            return False

        char = lines[yCheck][xCheck]
        expectedChar = scanFor.pop()

        if char != expectedChar:
            return False

    return True


def scan_line_v2(lines, x, y, xOffset):
    foundM, foundS = False, False

    for i in [0, 2]:
        yCheck = y+i-1
        xCheck = x+xOffset+(i*-xOffset)

        if (yCheck > len(lines)-1 or
            yCheck < 0 or
            xCheck > len(lines[yCheck])-1 or
                xCheck < 0):
            return False

        char = lines[yCheck][xCheck]

        if char == 'S':
            foundS = True
        if char == 'M':
            foundM = True

    return foundM and foundS


def solve_a(file):
    lines = parse_data(file)

    matches = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            char = lines[y][x]

            if char == 'X':
                found_matches = check_for_match(lines, x, y)
                matches += found_matches

    return matches


def solve_b(file):
    lines = parse_data(file)

    matches = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            char = lines[y][x]

            if char == 'A':
                found_match = check_for_match_v2(lines, x, y)
                if found_match:
                    matches += 1

    return matches


def run_a():
    test_result = solve_a("test.txt")
    test(test_result, 4)

    test_result = solve_a("test1.txt")
    test(test_result, 18)

    result = solve_a("data.txt")
    print(result)


def run_b():
    test_result = solve_b("test2.txt")
    test(test_result, 9)

    test_result = solve_b("test1.txt")
    test(test_result, 9)

    result = solve_b("data.txt")
    print(result)


run_a()
run_b()
