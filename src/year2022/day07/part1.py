from src.common.common import get_lines


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent
        self.cached_size = None

    def size(self):
        if self.cached_size is not None:
            return self.cached_size

        total = 0
        for child in self.children:
            if isinstance(child, File):
                total += child.size
            elif isinstance(child, Folder):
                total += child.size()
        self.cached_size = total
        return total


class File:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent


def main():
    lines = get_lines()

    folders = {}

    current_folder = None

    for line in lines:
        if line.startswith('$'):
            _, command = line.split('$ ')
            if command.startswith('cd'):
                _, folder_name = command.split(' ')
                if folder_name == '..':
                    current_folder = current_folder.parent
                elif folder_name == '/':
                    if folder_name not in folders:
                        folders[folder_name] = Folder(folder_name)
                    current_folder = folders[folder_name]
                else:
                    if folder_name not in folders:
                        folders[folder_name] = Folder(folder_name, current_folder)
                    current_folder = folders[folder_name]
            elif command.startswith('ls'):
                # no-op
                ...
        else:
            size_or_dir, name = line.split(' ')
            if size_or_dir == 'dir':
                folder = Folder(name, current_folder)
                current_folder.children.append(folder)
                folders[name] = folder
            else:
                current_folder.children.append(File(name, int(size_or_dir), current_folder))

    total = 0

    for name, folder in folders.items():
        if folder.size() <= 100000:
            total += folder.size()

    print(total)


if __name__ == "__main__":
    main()
