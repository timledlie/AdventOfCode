# a filesystem is the tree of directories starting at / and contains a size of all files,
# a lsit of directories, and a total size
# directories is a list of references to all the directories
class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.directories = {}
        self.file_size = 0
        self.total_size = 0


root = Directory("/", None)
current_directory = root

with open("input.txt") as file:
    for line in file.readlines()[1:]:
        line = line.strip()
        if line == '$ ls':
            state = 'listing-dir'
        elif line[:4] == '$ cd':
            if line == '$ cd ..':
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.directories[line[5:]]
        elif line[:3] == 'dir':
            dir_name = line[4:]
            current_directory.directories[dir_name] = Directory(dir_name, current_directory)
        else:
            file_size, file_name = line.split()
            current_directory.file_size += int(file_size)


def get_dir_total_size(d: Directory):
    subdirs_total = 0
    for subdir in d.directories.values():
        subdirs_total += get_dir_total_size(subdir)
    return d.file_size + subdirs_total


def get_part1_answer(d: Directory):
    answer = 0
    size = get_dir_total_size(d)
    if size <= 100000:
        answer = size
    for sub_dir in d.directories.values():
        answer += get_part1_answer(sub_dir)
    return answer


all_dir_sizes = []
def get_all_dir_sizes(d: Directory):
    all_dir_sizes.append(get_dir_total_size(d))
    for subdir in d.directories.values():
        get_all_dir_sizes(subdir)


free_space = 70000000 - get_dir_total_size(root)
needed = 30000000 - free_space
get_all_dir_sizes(root)
all_dir_sizes.sort()
for size in all_dir_sizes:
    if size >= needed:
        print(size)
        break
