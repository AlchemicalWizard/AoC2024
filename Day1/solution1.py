
def parse_data(filename):
    file = open(filename)
    lines = file.readlines()
    
    listA, listB = [], []
    for line in lines:
        a, b = line.split("   ")
        listA.append(int(a))
        listB.append(int(b.replace("\n", "")))
    
    return listA, listB

def test(input, expected):
    if(input != expected):
        raise Exception("Test failed, expected " + expected + " but received " + input)
    print("test passed")

def bubble_sort_list(inputList):
    index = len(inputList)//2
    sortA, sortB = [], []
    comparer = inputList[index]
    
    for i, value in enumerate(inputList):
        if(i == index):
            continue
        
        if(value > comparer):
            sortB.append(value)
        else:
            sortA.append(value)
            
    if(len(sortA) >= 2):
        sortA = bubble_sort_list(sortA)
    if(len(sortB) >= 2):
        sortB = bubble_sort_list(sortB)
    
    sortA.append(comparer)
    
    return sortA + sortB

def calculate_distances(a, b):
    distances = []
    for i, value in enumerate(a):
        distances.append(abs(value - b[i]))
        
    return distances
    
def calculate_similarity(listA, listB):
    similarity = 0
    for a in listA:
        similarity += a * len([i for i, b in enumerate(listB) if a == b])
        
    return similarity

def prepare_lists(file):
    a, b = parse_data(file)
    
    a = bubble_sort_list(a)
    b = bubble_sort_list(b)
    
    return a, b
    
def solve_a(file):
    a, b = prepare_lists(file)
    
    distances = calculate_distances(a, b)
    
    return sum(distances)

def solve_b(file):
    a, b = prepare_lists(file)
    
    return calculate_similarity(a, b)

def run_a():
    test_result = solve_a("test.txt")

    test(test_result, 11)

    result = solve_a("data.txt")
    print(result)

def run_b():
    test_result = solve_b("test.txt")

    
    test(test_result, 31)

    result = solve_b("data.txt")
    print(result)


run_a()
run_b()
