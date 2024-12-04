

def parse_data(filename):
    file = open(filename)
    lines = file.readlines()
    
    return lines

def test(input, expected):
    if(input != expected):
        raise Exception("Test failed, expected " + str(expected) + " but received " + str(input))
    print("test passed")
    
def check_report_part1(report):
    values = [int(string) for string in report.replace("\n", "").split(" ")]
    
    status = (values[0] > values[1]) - (values[0] < values[1]) 
    
    if not status or abs(values[0] - values[1]) > 3:
        return False
    
    for i, value in enumerate(values[2:]):
        previousValue = values[i+1]
        if (previousValue > value) - (previousValue < value) != status or abs(previousValue - value) > 3:
            return False
    return True

def check_report_for_error(values):
    status = (values[0] > values[1]) - (values[0] < values[1]) 
    
    if not status or abs(values[0] - values[1]) > 3:
        return 0
    
    for i, value in enumerate(values[2:]):
        previousValue = values[i+1]
        if (previousValue > value) - (previousValue < value) != status or abs(previousValue - value) > 3:
            return i+2
    return -1

def check_report_part2(report):
    values = [int(string) for string in report.replace("\n", "").split(" ")]
    
    result = check_report_for_error(values)
    
    if result == -1:
        return True
    
    for i in range(len(values)):
        valuesCopy = values.copy()
        valuesCopy.pop(i)
        
        newResult = check_report_for_error(valuesCopy)
        
        if newResult == -1:
            return True
        
    return False

def solve_a(file):
    reports = parse_data(file)
    
    safeReports = 0
    for report in reports:
        if check_report_part1(report):
            safeReports += 1
        
    return safeReports

def solve_b(file):
    reports = parse_data(file)
    
    safeReports = 0
    for report in reports:
        if check_report_part2(report):
            safeReports += 1
        
    return safeReports


def run_a():
    test_result = solve_a("test.txt")

    test(test_result, 2)

    result = solve_a("data.txt")
    print(result)


def run_b():
    test_result = solve_b("test.txt")

    test(test_result, 4)

    result = solve_b("data.txt")
    print(result)

run_a()
run_b()
