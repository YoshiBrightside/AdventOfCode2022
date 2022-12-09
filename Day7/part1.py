class File_or_Dir:
    def __init__(self, name = None, size = None):
        name = name
        size = size
        elems = []

    def get_size(self):
        if self.size is None:
            self.size = 0
            for e in self.elems:
                self.size += e.get_size()
        return self.size

    def add_elem(self, e):
        self.elems.append(e)
        self.size += e.get_size()

def main():

if __name__ == "__main__":
   main()