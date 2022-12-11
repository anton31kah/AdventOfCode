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
    lines = get_lines('')

    folders = {}

    current_folder = None
    current_path = []

    for line in lines:
        match line.split(' '):
            case ['$', 'cd', '..']:
                current_path.pop()
                current_folder = current_folder.parent
            case ['$', 'cd', '/']:
                current_path = ['/']
                current_path_name = ':'.join(current_path)
                if current_path_name not in folders:
                    folders[current_path_name] = Folder(current_path_name)
                current_folder = folders[current_path_name]
            case ['$', 'cd', folder_name]:
                current_path.append(folder_name)
                current_path_name = ':'.join(current_path)
                if current_path_name not in folders:
                    folders[current_path_name] = Folder(current_path_name, current_folder)
                current_folder = folders[current_path_name]
            case ['$', 'ls', *_]:
                # no-op
                ...
            case ['dir', name]:
                current_path_name = ':'.join(current_path + [name])
                folder = Folder(name, current_folder)
                current_folder.children.append(folder)
                folders[current_path_name] = folder
            case [size, name]:
                current_folder.children.append(File(name, int(size), current_folder))

    total = 0

    for name, folder in folders.items():
        # print(name, folder.size())
        if folder.size() <= 100000:
            total += folder.size()

    print(total)


if __name__ == "__main__":
    main()
