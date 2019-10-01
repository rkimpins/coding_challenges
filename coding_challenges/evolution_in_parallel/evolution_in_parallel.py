# Problem taken from https://open.kattis.com/problems/evolution


# Given two lists, returns true if the first list is a subsequence of the second
# ex [1, 2, 3] - [1, 4, 2, 3]: True
# This code is taken from stackoverflow: Forcetti  
def is_subsequence(a, b):
    idx_b = 0
    for v in a:
        try:
            b[idx_b:].index(v)
        except ValueError:
            return False
        idx_b += 1
    return True

# Test cases for is_subsequence
def test_is_subsequence():
    print("Testing is_subsequence()")
    print("Test 1")
    assert is_subsequence([1,2], [1,2,3])
    print("Test 2")
    assert is_subsequence([1,2], [1,2,4])
    print("Test 3")
    assert is_subsequence([1,2,4], [1,2,3,4])
    print("Test 4")
    assert is_subsequence([1,2,3], [1,2,3,4])
    print("Test 5")
    assert is_subsequence([], [1,2,3])
    print("Test 6")
    assert is_subsequence([1,2,3], [1,2,3])
    print("Test 7")
    assert is_subsequence([1,2,3], [1,2,3])

# Test cases for insert_stage
def test_insert_stage():
    x = [[1], [1,2], [1,2,3,4]]
    y = [1,2,3]
    assert insert_stage(y, x)
    y = [1,2,4]
    assert insert_stage(y, x)

# Given a potential stage in a path,
# If possible, inserts it into the path, returning true
# Or does not insert it, and returns false
def insert_stage(stage, path):
    # Stage belongs at front
    if is_subsequence(stage, path[0]):
        path.insert(0, stage)
        return True
    # Stage belongs at back
    if is_subsequence(path[-1], stage):
        path.insert(-1, stage)
        return True
    # Stage belongs somewhere in evolution
    for i in range(len(path)-1):
        x1 = path[i]
        x2 = path[i+1]
        if is_subsequence(stage, x2) and is_subsequence(x1, stage):
            path.insert(i+1, stage)
            return True
    # Stage doesn't belong in path
    return False

# Print formated fossil
def print_fossil(fossil):
    for item in fossil:
        print(item, end='')
    print()

# Print formated path excluding last element
def print_path(path):
    for fossil in path:
        print_fossil(fossil)

def check_if_parallel(fossils, current):
    path1 = [current]
    path2 = [current]

    # Check that there is any valid path
    for fossil in fossils:
        if not is_subsequence(fossil, current):
            print("impossible")
            return

    # Try to build two paths for the fossils
    # If we need more then two paths, return impossible
    for fossil in fossils:
        if not insert_stage(fossil, path1):
            if not insert_stage(fossil, path2):
                print("impossible")
                return

    # Remove temporary last element representing current fossil
    del path1[-1]
    del path2[-1]
    
    # Print the lengths of our two paths
    if len(path2) > len(path1):
        print(len(path1), end=' ')
        print(len(path2))
        print_path(path1)
        print_path(path2)
    else:
        print(len(path2), end=' ')
        print(len(path1))
        print_path(path2)
        print_path(path1)

# Like check_if_parallel, but only returns true or false
def mock_check_if_parallel(fossils, current):
    path1 = [current]
    path2 = [current]
    # Check that there is any valid path
    for fossil in fossils:
        if not is_subsequence(fossil, current):
            return False

    # Try to build two paths for the fossils
    # If we need more then two paths, return impossible
    for fossil in fossils:
        if not insert_stage(fossil, path1):
            if not insert_stage(fossil, path2):
                return False
    
    return True

def test_check_if_parallel():
    print("Testing check_if_parallel")
    print("Test 1")
    current = ['A', 'A', 'C', 'C', 'M', 'M', 'A', 'A']
    fossils = [
        ['A', 'C', 'A'],
        ['M', 'M'],
        ['A', 'C', 'M', 'A', 'A'],
        ['A', 'A'],
        ['A']
    ]
    assert mock_check_if_parallel(fossils, current)
    print("Test 2")
    current = ['A', 'C', 'M', 'A']
    fossils = [['A', 'C', 'M'], ['A', 'C', 'A'], ['A', 'M', 'A']]
    assert mock_check_if_parallel(fossils, current) == False
    print("Test 3")
    current = ['A', 'M']
    fossils= [['M', 'A']]
    print("Test 4")
    current = ['A', 'A', 'A', 'A', 'A', 'A']
    fossils = [
        ['A', 'A'], 
        ['A', 'A', 'A'], 
        ['A'], 
        ['A', 'A', 'A', 'A', 'A']
    ]
    assert mock_check_if_parallel(fossils, current)


def main():
    TESTING = False
    if TESTING:
        test_check_if_parallel()
    else:
        num = int(input())
        current = list(input())
        fossils = list()
        for _ in range(num):
            fossils.append(list(input()))
        check_if_parallel(fossils, current)

main()