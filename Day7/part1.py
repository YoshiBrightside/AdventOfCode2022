from collections import deque

class Node:
    def __init__(self, name = None, size = '0', parent = None):
        self.name = name
        self.size = 0 if size == 'dir' else int(size)
        self.parent = parent
        self.elems = {}

    # Updates node's self and parent size
    def add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)

    # Adds a child node to an existing node
    def add_elem(self, name, e):
        self.elems[name] = e
        self.add_size(e.size)

    # String visualization
    def to_str(self, recursive = False):
        s = str(self.name) + ' ' + str(self.size)
        if recursive:
            for k, v in self.elems.items():
                s = s + '\n\t' + k + v.to_str()
        return s

def create_dir():
    input() # We ignore the first "$ cd /"
    root = Node(name='/')
    line, cur_file = input().split(' '), root
    while line[0]:
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '..':
                cur_file = cur_file.parent
            else:
                cur_file = cur_file.elems[line [2]]
        elif line[0] != '$':
            cur_file.add_elem(line[1], Node(name=line[1], size=line[0], parent=cur_file))
        line = input().split(' ')
    return root

def get_directories_with_max_size(root, size):
    ans, next_nodes = [], deque([root])
    while next_nodes:
        cur_node = next_nodes.pop()
        if cur_node.size <= size and cur_node.elems:
            ans.append(cur_node)
        for e in cur_node.elems.values():
            next_nodes.append(e)
    return ans

def main():
    root = create_dir()
    directories = get_directories_with_max_size(root, 100000)
    ans = 0
    for dir in directories:
        ans += dir.size
    print(ans)

if __name__ == "__main__":
   main()