# Problem taken from https://open.kattis.com/problems/collapse


def propogate(nNode, isl, need):
    for supply in isl[nNode]:
        if need > 0 and need < supply:
            print()

def main():
    nIsl = int(input())
    isl = dict()
    need = dict()
    for x in range(1, nIsl+1):
        isl[x] = list()
    
    for node in range(1, nIsl+1):
        inputs = list(map(int, input().split()))
        need[node] = inputs[0]
        connected = inputs[1]
        for incoming in range(connected):
            x = inputs[2+incoming*2]
            y = inputs[2+incoming*2+1]
            isl[x].append((node, y))

main()