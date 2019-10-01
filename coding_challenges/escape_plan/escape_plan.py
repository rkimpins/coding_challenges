# problem taken from https://open.kattis.com/problems/escapeplan
import math

# Taken from stack overflow
# Calculates the distance between two points
def point_distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def print_result(scenario, sec5, sec10, sec20):
    print("Scenario " + str(scenario))
    print("In 5 seconds " + str(sec5) + " robot(s) can escape")
    print("In 10 seconds " + str(sec10) + " robot(s) can escape")
    print("In 20 seconds " + str(sec20) + " robot(s) can escape")
    print()


# Given our robots and holes, and assuming each robot tries to travel
# to the nearest hole, and only to that hole, outputs how many
# Robots can survive for 5, 10, and 20 seconds
def solve_to_nearest(scenario, robots, holes):
    result5 = set()
    result10 = set()
    result20 = set()
    for robot in robots:
        min_distance = point_distance(robot, holes[0])
        min_hole = holes[0]
        for hole in holes:
            distance = point_distance(robot, hole)
            if  distance < min_distance:
                min_hole = hole
                min_distance = distance
        if min_distance <= 50:
            result5.add(min_hole)
        if min_distance <= 100:
            result10.add(min_hole)
        if min_distance <= 200:
            result20.add(min_hole)
    print_result(scenario, len(result5), len(result10), len(result20))
        

def solve_greedy(scenario, robots, holes):
    print()


def main():
    scenario = 1
    while(True):
        num_robots = int(input())
        if num_robots == 0:
            break
        robots = list()
        for _ in range(num_robots):
            x = input().split()
            robots.append( (float(x[0]), float(x[1])) )
        num_holes = int(input())
        holes = list()
        for _ in range(num_holes):
            x = input().split()
            holes.append( (float(x[0]), float(x[1])) )
        solve_to_nearest(scenario, robots, holes)
        scenario += 1

main()