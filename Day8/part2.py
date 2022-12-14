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
    # Create a scenic score for all trees in forest
    scenic_scores = [[1 for _ in range(len(forest[0]))] for _ in range(len(forest))]
    forest_h, forest_w = len(forest), len(forest[0])
    # Calculate scenic score for all trees from right to left and then left to right
    for h in range(forest_h):
        for w in range(-forest_w + 1, forest_w):
            # Set score to 0 and restarts queue if at beggining or end of forest width
            if w == 0 or abs(w) == forest_w - 1: scenic_scores[h][abs(w)], tall_tree_indexes = 0, deque([])
            # Pop all smaller trees on our stack
            while tall_tree_indexes and forest[h][abs(w)] > forest[h][tall_tree_indexes[-1]]: tall_tree_indexes.pop()
            # Get number of trees between current tree and bigger/equal tree
            if tall_tree_indexes: 
                scenic_scores[h][abs(w)] *= abs(abs(w) - tall_tree_indexes[-1]) 
            # Get number of trees between current tree and end of forest
            else: 
                scenic_scores[h][abs(w)] *= w + forest_w - 1 if w <= 0 else w
            tall_tree_indexes.append(abs(w))
    # Calculate scenic score for all trees bottom-up and then top-down
    for w in range(forest_w):
        for h in range(-forest_h + 1, forest_h):
            # Set score to 0 and restarts queue if at beggining or end of forest height
            if h == 0 or abs(h) == forest_h - 1: scenic_scores[abs(h)][w], tall_tree_indexes = 0, deque([])
            # Pop all smaller trees on our stack
            while tall_tree_indexes and forest[abs(h)][w] > forest[tall_tree_indexes[-1]][w]: tall_tree_indexes.pop()
            # Get number of trees between current tree and bigger/equal tree
            if tall_tree_indexes: 
                scenic_scores[abs(h)][w] *= abs(abs(h) - tall_tree_indexes[-1])
            # Get number of trees between current tree and end of forest
            else: 
                scenic_scores[abs(h)][w] *= h + forest_h - 1 if h <= 0 else h
            tall_tree_indexes.append(abs(h))
    return scenic_scores

def main():
    forest = get_forest()
    scenic_scores = get_scenic_score(forest)
    ans = max(max(x) for x in scenic_scores)
    print(ans)

if __name__ == "__main__":
   main()
