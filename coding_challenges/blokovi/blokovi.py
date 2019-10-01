# This is a solution to https://open.kattis.com/problems/blokovi
# Given N blocks with a certain mass and length=2
# Find the largest horizontal distance we can reach by stacking them
# NOTICE: We will be stacking them with the largest block on top
# If we use the top block to rebalance to the left, we can have a 
# smaller center block sticking out further
# We are not just stacking them in one direction

# Given two arrays of sub_masses and sub_centers of blocks,
# Returns the barycenter of those blocks
def barycenter(sub_masses, sub_centers):
    #print(sub_centers, sub_masses)
    sum_masses = sum(sub_masses)
    barycenter = 0
    for mass, center in zip(sub_masses, sub_centers):
        barycenter += mass * center
    barycenter /= sum_masses
    return barycenter

# Given block masses, stacks them moving upwards and to the left
# with the larger block on top then returns the total mass and
# the distance from the barycenter to the outermost edge
def bc_right(block_masses):
    block_centers = [0 for x in range(len(block_masses))]

    for start in range(len(block_masses)-1, 0, -1):
        # Get the subset of blocks we will work on
        sub_masses = block_masses[start:]
        sub_centers = block_centers[start:]
        block_centers[start-1] = barycenter(sub_masses, sub_centers)-1
    #print(block_centers)
    #print(barycenter(block_masses, block_centers))
    return sum(block_masses), abs(block_centers[0] - barycenter(block_masses, block_centers)) + 1

# Given block masses, stacks them moving upwards and to the left
# with the larger blocks on top, then returns the distance
# from the topleft blocks right edge to our bottom blocks right edge
def bc_left(block_masses, top_mass):
    block_masses.append(top_mass)
    block_centers = [0 for x in range(len(block_masses))]

    for start in range(len(block_masses)-1, 0, -1):
        # Get the subset of blocks we will work on
        sub_masses = block_masses[start:]
        sub_centers = block_centers[start:]
        block_centers[start-1] = barycenter(sub_masses, sub_centers)-1
    #print(block_centers)
    return abs(block_centers[0] + 1)

# We should be able to quickly find a barycenter by taking
# The previous barycenters numerator and denominator
# Bary center = num + mi+1 * center(i+1) ) / denom + mi+1

def calculate_distance(block_masses, div):
    top_mass, distance1 = bc_right(block_masses[div:])
    distance2 = bc_left(block_masses[:div], top_mass)
    #print("top_mass:", str(top_mass))
    #print("distance1:", str(distance1))
    #print("distance2:" + str(distance2))
    return(distance1 + distance2)

def calculate_max_distance(block_masses):
    result = 0
    for div in range(1, len(block_masses)):
        #print(calculate_distance(block_masses, div))
        result = max(result, calculate_distance(block_masses, div))
    return result

def main():
    testing = False

    if not testing:
        # Get the appropriate input
        num_blocks = int(input())
        block_masses = list()
        for _ in range(num_blocks):
            block_masses.append(int(input()))
        print(calculate_max_distance(block_masses))
    else:
        print("Testing [1, 1] : 1")
        block_masses = [1, 1]
        print("Passed")
        assert calculate_max_distance(block_masses) == 1
        print("Testing [1, 1, 1] : 1.5")
        block_masses = [1, 1, 1]
        assert calculate_max_distance(block_masses) == 1.5
        print("Passed")
        print("Testing [1, 1, 9] : 1.9")
        block_masses = [1, 1, 9]
        assert calculate_max_distance(block_masses) == 1.9
        print("Passed")


    ''' Take 1 block
    Find it's center
    Add the distance to the right of that single block
    Add an additional block, the right side lined up with our center
    Calculate the center ofthese 2 blocks
    Add the local distance to the right of the bottem block
    Repeat this for everything except the last block
    '''
main()