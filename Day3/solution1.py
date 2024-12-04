import re

def parse_data(filename):
    file = open(filename)
    return file.read()

def test(input, expected):
    if(input != expected):
        raise Exception("Test failed, expected " + str(expected) + " but received " + str(input))
    print("test passed")

def solve_a(file):
    string = parse_data(file)
    matches = re.findall( r'mul\(\d{1,3},\d{1,3}\)', string)
    
    result = 0
    
    for match in matches:
        match = match.replace("mul(", "").replace(')', "")
        a, b = match.split(",")
        
        result += int(a) * int(b)
        
    return result


def solve_b(file):
    string = parse_data(file)
    matches = re.findall( r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", string)

    result = 0
    
    mulEnabled = True
    for match in matches:
        if match == "do()":
            mulEnabled = True
        elif match == "don't()":
            mulEnabled = False
        elif mulEnabled:
            match = match.replace("mul(", "").replace(')', "")
            a, b = match.split(",")
        
            result += int(a) * int(b)
    return result

def run_a():
    test_result = solve_a("test.txt")

    test(test_result, 161)

    result = solve_a("data.txt")
    print(result)

def run_b():
    test_result = solve_b("test2.txt")

    test(test_result, 48)

    result = solve_b("data.txt")
    print(result)

run_a()
run_b()
