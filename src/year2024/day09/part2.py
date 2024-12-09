from src.common.common import get_lines


class File:
    def __init__(self, id: int, size: int):
        self.id = id
        self.size = size
        self.initial_size = size
    
    def __str__(self):
        return format(self, 'l')
    
    def __format__(self, format_spec):
        match format_spec:
            case 's':
                if self.size >= self.initial_size:
                    return f'{self.id}' * self.size
                else:
                    return f'{self.id}' * self.size + '.' * (self.initial_size - self.size)
            case 'l':
                return f'File(id={self.id}, size={self.size})'
        raise ValueError('File string formatting allows only `l` for long and `s` for short as options!')

    def __repr__(self):
        return str(self)


class FreeSpace:
    def __init__(self, space: int):
        self.space = space
        self.files: dict[int, File] = {}
    
    def add_file(self, file: File):
        if self.space <= 0:
            return False
        if file.id in self.files:
            self.files[file.id].size += file.size
        else:
            self.files[file.id] = File(file.id, file.size)
        self.space -= file.size
        file.size = 0
        return True
    
    def __str__(self):
        return format(self, 'l')
    
    def __format__(self, format_spec):
        match format_spec:
            case 's':
                files_str = ''.join(format(f, 's') for f in self.files.values())
                return files_str + ('.' * self.space)
            case 'l':
                files_str = ','.join(map(str, self.files.values()))
                return f'FreeSpace(space={self.space}, files=[{files_str}])'
        raise ValueError('FreeSpace string formatting allows only `l` for long and `s` for short as options!')

    def __repr__(self):
        return str(self)


class Disk:
    def __init__(self):
        self.things: list[File | FreeSpace] = []
    
    def add(self, thing: File | FreeSpace):
        self.things.append(thing)

    def checksum(self):
        result = 0

        idx = 0

        for thing in self.things:
            if type(thing) is File:
                # print('file', thing.id, 'size', thing.size)
                if thing.size >= 1:
                    for n in range(thing.size):
                        result += thing.id * idx
                        # print(f'{thing.id} * {idx}')
                        idx += 1
                else:
                    idx += (thing.initial_size - thing.size)
            elif type(thing) is FreeSpace:
                # print('space', thing.space)
                for file in thing.files.values():
                    # print('space file', file.id, 'size', file.size)
                    for n in range(file.size):
                        result += file.id * idx
                        # print(f'{file.id} * {idx}')
                        idx += 1
                idx += thing.space

        return result

    def __str__(self):
        return format(self, 'l')
    
    def __format__(self, format_spec):
        match format_spec:
            case 's':
                return ''.join(f'{t:s}' for t in self.things)
            case 'l':
                return '\n'.join(map(str, self.things))
        raise ValueError('Disk string formatting allows only `l` for long and `s` for short as options!')
    
    def __repr__(self):
        return str(self)


def parse_line(line: str) -> Disk:
    file_id = 0
    reading_file = True

    output = Disk()

    for char in line:
        num = int(char)

        if reading_file:
            output.add(File(file_id, num))
            file_id += 1
        else:
            output.add(FreeSpace(num))
        
        reading_file = not reading_file
    
    return output


def main():
    lines = get_lines('')

    disk: Disk = parse_line(lines[0])

    # print(f'{disk:l}')
    # print(f'{disk:s}')

    total_things = len(disk.things)
        
    # FSFS  -> len 4 -> file at 2 (len-2)
    # FSFSF -> len 5 -> file at 4 (len-1)
    general_last_file_index = total_things - 2 if total_things % 2 == 0 else total_things - 1

    for file_idx in range(general_last_file_index, -1, -2):
        file = disk.things[file_idx]

        for free_space_idx in range(1, file_idx, 2):
            free_space = disk.things[free_space_idx]

            if free_space.space >= file.size:
                free_space.add_file(file)
                break
        
        # print(f'{disk:s}')

    print(disk.checksum())


if __name__ == "__main__":
    main()
