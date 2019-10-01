# Problem taken from https://open.kattis.com/problems/kitchencombinatorics
from collections import defaultdict

# Given the ingredients for our three meals, returns the number of combinations
# with consideration to ingredient invariance
def combinations(s_ingr, m_ingr, d_ingr, brands):
    result = 1
    for ingredient in s_ingr:
        result *= brands[ingredient-1]
    for ingredient in m_ingr:
        if ingredient not in s_ingr:
            result *= brands[ingredient-1]
    for ingredient in d_ingr:
        if ingredient not in s_ingr and ingredient not in m_ingr:
            result *= brands[ingredient-1]
    return result

# Given our possible dishes, brands, and incompatible dishes, 
# Finds all possible dinner experiences we could provide
def calculate_experiences(s, m, d, si, mi, di, b, inc):
    result = 0
    for sindex, sdish in enumerate(si):
        for mindex, mdish in enumerate(mi):
            for dindex, ddish in enumerate(di):
                if sindex+1 not in inc[mindex+s+1] and sindex+1 not in inc[dindex+s+m+1] and mindex+1 not in inc[dindex+s+m+1]:
                    result += combinations(sdish, mdish, ddish, b)
    if result < 10**18:
        return result
    else:
        return "too many"

# pretty prints the inputs that we recieve
def print_inputs(r, s, m, d, n, b, si, mi, di, inc):
    print("Num ingredients:", r, ", Num starters:", s, ", Num mains:", m, ", Num desserts:", d, ", Num incompatibles:", n)
    print("Brands:", b)
    print("Starter:", si)
    print("Main:", mi)
    print("Dessert:", di)
    print("Incompatiables:", inc)

# Get our inputs and properly format them
def get_inputs():
    # Get our indexing inputs
    r, s, m, d, n = list(map(int, input().split()))
    # Get our number of different brands
    b = list(map(int, input().split()))
    # Get our lists of dishs ingredients
    si = list()
    mi = list()
    di = list()
    for _ in range(s):
        si.append(list(map(int, input().split()))[1:])
    for _ in range(m):
        mi.append(list(map(int, input().split()))[1:])
    for _ in range(d):
        di.append(list(map(int, input().split()))[1:])
    # Get incompatible dishses nad put them into a dictionary for easy access
    inc = defaultdict(list)
    for _ in range(n):
        item1, item2 = list(map(int, input().split()))
        inc[item1].append(item2)
        inc[item2].append(item1)
    return r, s, m, d, b, si, mi, di, inc

# Takes a raw input, formats it, and tests it against an expected value
def test(test_num, input, expected):
    if TESTING:
        print("Test 1")
        print("Input:")
        print('''6 1 1 1 0
            2 3 1 5 3 2
            2 1 2
            3 3 4 5
            1 6''')
        print("Expected: 180")
        if calculate_experiences(1, 1, 1, [1, 2], [3, 4, 5], [1, 6], \
                [2, 3, 1, 5, 3, 2], defaultdict()) == 180:
            print("Test Passed")
        else:
            print("Test Failed")


# r: number of ingredients
# s,m,d: number of available starter dishes, main dishes, desserts
# n: number of pairs of dishes that donot go well together
# b: number of brands of an ingredient
# si: ingredient list for each starter dish
# mi: ingredient list for each main dish
# di: ingredient list for each dessert dish
# inc: dictionary of incompatible dishes
def main():
    TESTING = False
    if not TESTING:
        r, s, m, d, b, si, mi, di, inc = get_inputs()
        print(calculate_experiences(s, m, d, si, mi, di, b, inc))

    if TESTING:
        # Test 1
        print("Test 1")
        print("Input:")
        print(" 6 1 1 1 0\n 2 3 1 5 3 2\n 2 1 2\n 3 3 4 5\n 1 6")
        print("Expected: 180")
        if calculate_experiences(1, 1, 1, [[1, 2]], [[3, 4, 5]], [[6]], \
                [2, 3, 1, 5, 3, 2], defaultdict(list)) == 180:
            print("Test Passed")
        else:
            print("Test Failed")
        # Test 2
        print("Test 2")
        print("Input:")
        print(" 3 2 2 1 1\n 2 3 2\n 1 1\n 1 2\n 1 2\n 1 3\n 1 1\n 2 3")
        print("Expected: 22")
        inc = defaultdict(list)
        inc[2].append(3)
        inc[3].append(2)
        if calculate_experiences(2, 2, 1, [[1], [2]], [[2], [3]], [[1]], \
                [2, 3, 2], inc) == 22:
            print("Test Passed")
        else:
            print("Test Failed")
        # Test 3
        print("Test 3")
        print("Input:")
        print(" 3 1 1 1 1\n 5 5 5\n 3 1 2 3\n 3 1 2 3\n 3 1 2 3\n 2 1")
        print("Expected: 22")
        inc = defaultdict(list)
        inc[1].append(2)
        inc[2].append(1)
        if calculate_experiences(1, 1, 1, [[1, 2, 3]], [[1, 2, 3]], [[1, 2, 3]], \
                [5, 5, 5], inc) == 0:
            print("Test Passed")
        else:
            print("Test Failed")
        # Test 4
        print("Test 4")
        print("Input:")
        print(" 10 1 1 1 0\n 100 100 100 100 100 100 100 100 100 100\n 4 1 2 3 4\n 3 5 6 7\n 3 8 9 10")
        print("Expected: too many")
        inc = defaultdict(list)
        if calculate_experiences(1, 1, 1, [[1, 2, 3, 4]], [[5, 6, 7]], [[8, 9, 10]], \
                [100, 100, 100, 100, 100, 100, 100, 100, 100, 100], inc) == "too many":
            print("Test Passed")
        else:
            print("Test Failed")
main()
