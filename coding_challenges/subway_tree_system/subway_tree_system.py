# problem taken from https://open.kattis.com/problems/subway
# Given a subway system (in the form of a spanning tree), 
# we can explore by going out along a path, and when we reach the end
# we come back in.
# 0 = going out
# 1 = going in
# Given two such strings, find if they could encode the same subway system
# 2
# 0010011101001011
# 0100011011001011
# 0100101100100111
# 0011000111010101
# same
# different

# Given two sequences of subway traversals, return true if they could be
# of the same subway system
def check_if_same_debug(str1, str2):
    # Strategy, break it into outgoing paths, then check if recursive calls if
    # they are in the other system
    print("check called with: ", str1, str2)

    # If our two strings are the Same, return True
    if str1 == str2:
        print("Strings are the same")
        return True

    if len(str1) != len(str2):
        print("Strings are not the same size")
        return False


    # Otherwise, break the graph into possible subgraphs, and compare them
    paths1 = break_root(str1)
    paths2 = break_root(str2)

    print("Broken into: ", paths1, paths2)

    # Check if our paths are broken down by break root
    if len(paths1) == 1 or len(paths2) == 1:
        # If our paths aren't broken down, check if the have a single leaving path
        print(str1[0], str1[-1], str2[0], str2[-1])
        if str1[0] == '0' and str1[-1] == '1' and str2[0] == '0' and str2[-1] == '1':
            print("Single path")
            return check_if_same(str1[1:-1], str2[1:-1])
        else:
            # If they aren't broken and aren't single, they are not the same
            print("Not broken or single")
            return False

    # If our two values are recursively the same, we can delete them
    for path1 in paths1[::-1]:
        for path2 in paths2[::-1]:
            if check_if_same(path1, path2):
                print("removing: ", path1, path2)
                paths1.remove(path1)
                paths2.remove(path2)
                break
    
    # If we have not deleted all paths by this point in time,
    # Our subways are not the same
    if len(paths1) == 0 and len(paths2) == 0:
        print("All paths deleted")
        return True
    else:
        print("Not all paths deleted")
        return False 
 
# Given two sequences of subway traversals, return true if they could be
# of the same subway system
def check_if_same(str1, str2):
    # Strategy, break it into outgoing paths, then check if recursive calls if
    # they are in the other system

    # If our two strings are the Same, return True
    if str1 == str2:
        return True

    if len(str1) != len(str2):
        return False


    # Otherwise, break the graph into possible subgraphs, and compare them
    paths1 = break_root(str1)
    paths2 = break_root(str2)


    # Check if our paths are broken down by break root
    if len(paths1) == 1 or len(paths2) == 1:
        # If our paths aren't broken down, check if the have a single leaving path
        if str1[0] == '0' and str1[-1] == '1' and str2[0] == '0' and str2[-1] == '1':
            return check_if_same(str1[1:-1], str2[1:-1])
        else:
            # If they aren't broken and aren't single, they are not the same
            return False

    # If our two values are recursively the same, we can delete them
    for path1 in paths1[::-1]:
        for path2 in paths2[::-1]:
            if check_if_same(path1, path2):
                paths1.remove(path1)
                paths2.remove(path2)
                break
    
    # If we have not deleted all paths by this point in time,
    # Our subways are not the same
    if len(paths1) == 0 and len(paths2) == 0:
        return True
    else:
        return False 

# Given a traveral, break it into the traversals that leave the root
def break_root(str):
    level = 0
    path = ""
    paths = list()
    for char in str:
        if char == '0':
            path += char
            level += 1
        elif char == '1':
            path += char
            level -= 1
        if level == 0:
            paths.append(path)
            path = ""
    return(paths)

def main():
    TESTING = False
    DEBUG = False
    
    if not TESTING:
        testCases = int(input())
        for _ in range(testCases):
            str1 = input()
            str2 = input()
            if DEBUG:
                result = check_if_same_debug(str1, str2)
            else:
                result = check_if_same(str1, str2)
            if result:
                print("same")
            else:
                print("different")
    
    if TESTING:
        # Test 1
        str1 = "0010011101001011"
        str2 = "0100011011001011"
        print("Testing " + str1 + " against " + str2)
        print("Expected True")
        if DEBUG:
            result = check_if_same_debug(str1, str2)
        else:
            result = check_if_same(str1, str2)
        print("Got " + str(result))
        if result == True:
            print("Test Passed")
        else:
            print("Test Failed")

        # Test 2
        str1 = "0100101100100111"
        str2 = "0011000111010101"
        print("Testing " + str1 + " against " + str2)
        print("Expected False")
        if DEBUG:
            result = check_if_same_debug(str1, str2)
        else:
            result = check_if_same(str1, str2)
        print("Got " + str(result))
        if result == False:
            print("Test Passed")
        else:
            print("Test Failed")

main()