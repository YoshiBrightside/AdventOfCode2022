def get_forest():
    forest, line = [], input()
    while(line):
        forest.append([int(i) for i in line])
        line = input()
    return forest
        
def get_visible_trees(forest):
    visible_trees = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
    forest_h, forest_w = len(forest), len(forest[0])
    for h in range(forest_h):
        for w in range(-forest_w + 1, forest_w):
            if w == 0 or w == -forest_w + 1: tallest_tree_h = -1
            if tallest_tree_h < forest[abs(h)][abs(w)]: visible_trees[abs(h)][abs(w)] = 1
            tallest_tree_h = max(tallest_tree_h, forest[abs(h)][abs(w)])
    for w in range(forest_w):
        for h in range(-forest_h + 1, forest_h):
            if h == 0 or h == -forest_h + 1: tallest_tree_h = -1
            if tallest_tree_h < forest[abs(h)][abs(w)]: visible_trees[abs(h)][abs(w)] = 1
            tallest_tree_h = max(tallest_tree_h, forest[abs(h)][abs(w)])
    return visible_trees

def main():
    forest = get_forest()
    visible_trees = get_visible_trees(forest)
    ans = sum(sum(x) for x in visible_trees)
    print(ans)

if __name__ == "__main__":
   main()