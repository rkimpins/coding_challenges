# This is a solution to https://open.kattis.com/problems/peasoup
# We are simply checking restraunt menus and seeing if 
# they contain food items we want (pea soup, pancakes)
# Note that the menu items must match exactly
# 2 : Number of restraunts
# 2 : Number of menu items 
# q : at restraunt 1
# potatoes : menu item 1
# salad : menu item 2
# 3 : Number of menu items
# nymble : at restraunt 2
# pancakes : menu item 1
# pea soup : menu item 2
# punsch : menu item 3
def main():
    num_rest = int(input())
    valid_restraunt = False
    # Iterate over each restraunt
    for rest_index in range(0, num_rest):
        ps = False
        pc = False
        num_menu_items = int(input())
        rest_name = input()
        # Iterate over the menu items for that restraunt
        for menu_item_index in range(0, num_menu_items):
            menu_item = input()
            # Update flags for pea soup and pancakes
            if "pea soup" == menu_item:
                ps = True
            if "pancakes" == menu_item:
                pc = True
        # If menu items contain ps and pc, this restraunt is valid
        if pc and ps:
            valid_restraunt = True
            print(rest_name)
            break
    if not valid_restraunt:
        print("Anywhere is fine I guess")
main()
