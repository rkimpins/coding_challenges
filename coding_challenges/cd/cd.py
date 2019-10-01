def in_common_sets(A, B):
    print(len(A & B))

def in_common(A, B):
    i = 0
    j = 0
    result = 0
    while (i < len(A) and j < len(B)):
        # print(i, j)
        if (A[i] == B[j]):
            result += 1
            i += 1
            j += 1
        elif (A[i] > B[j]):
            j += 1
        else:
            i += 1
    print(result)

def main():
    filename = "cd_test_1.txt"
    file = open(filename)
    number = file.readline()
    number = number.split()
    set1 = set()
    set2 = set()
    list1 = []
    list2 = []
    for x in range(0, int(number[0])):
        line = file.readline()
        set1.add(line.strip())
        list1.append(line.strip())
    for x in range(0, int(number[1])):
        line = file.readline()
        set2.add(line.strip())
        list2.append(line.strip())
    # print(list1)
    # print(list2)
    in_common_sets(set1, set2)
    in_common(list1, list2)

main()