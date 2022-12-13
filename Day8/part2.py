from collections import deque

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

def get_scenic_score(forest):
    scenic_scores = [[1 for _ in range(len(forest[0]))] for _ in range(len(forest))]
    forest_h, forest_w = len(forest), len(forest[0])
    for h in range(forest_h):
        for w in range(forest_w):
            if h == 0 or w == 0 or h == forest_h - 1 or w == forest_w - 1:
                scenic_scores[h][w] = 0
                continue
            # Checks for trees up
            seen_trees = 0
            for i in reversed(range(h)):
                seen_trees += 1
                if forest[i][w] >= forest[h][w]: break
            scenic_scores[h][w] *= seen_trees
            # Checks for trees down
            seen_trees = 0
            for i in range(forest_h - h - 1):
                seen_trees += 1
                if forest[h + i + 1][w] >= forest[h][w]: break
            scenic_scores[h][w] *= seen_trees
            # Checks for trees left
            seen_trees = 0
            for i in reversed(range(w)):
                seen_trees += 1
                if forest[h][i] >= forest[h][w]: break
            scenic_scores[h][w] *= seen_trees
            # Checks for trees right
            seen_trees = 0
            for i in range(forest_w - w - 1):
                seen_trees += 1
                if forest[h][w + i + 1] >= forest[h][w]: break
            scenic_scores[h][w] *= seen_trees
    return scenic_scores

def main():
    forest = get_forest()
    scenic_scores = get_scenic_score(forest)
    for x in scenic_scores:
        print(x)
    ans = max(max(x) for x in scenic_scores)
    print(ans)

if __name__ == "__main__":
   main()
