import os

def generate_dir(dir_name):
    dir_path = os.getcwd() + '/' + dir_name
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path

def generate_file(path, name):
    file_path = path + '/' + name
    if not os.path.exists(file_path):
        open(file_path, 'x').close()
    return file_path

def main():
    dir_name = input('Type the name of the directory: ')
    dir_copies = int(input('Type the number of copies: '))
    file_parts = int(input('Type the number of part files on each directory: '))
    file_ext = input('Type the extension, without <.>, of the part files: ')
    for i in range(1, dir_copies + 1):
        new_dir_path = generate_dir(dir_name + str(i))
        for j in range(1, file_parts + 1):
            generate_file(new_dir_path, 'part' + str(j) + '.' + file_ext)

if __name__ == "__main__":
   main()