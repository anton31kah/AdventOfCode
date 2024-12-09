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
            self.files[file.id].size += 1
        else:
            self.files[file.id] = File(file.id, 1)
        file.size -= 1
        self.space -= 1
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
        self.empty_space_index = None
        self.last_file_index = None
    
    def add(self, thing: File | FreeSpace):
        self.things.append(thing)

    def calculate_empty_space_index(self):
        start = self.empty_space_index if self.empty_space_index is not None else 1
        # self.empty_space_index = next(i for i, x in enumerate(self.things) if type(x) is FreeSpace and x.space >= 1)
        
        for idx in range(start, len(self.things), 2):
            free_space = self.things[idx]
            if free_space.space >= 1:
                self.empty_space_index = idx
                return
        
        raise ValueError('No more free space')

    def calculate_last_file_index(self):
        total_things = len(self.things)
        
        # FSFS  -> len 4 -> file at 2 (len-2)
        # FSFSF -> len 5 -> file at 4 (len-1)
        general_last_file_index = total_things - 2 if total_things % 2 == 0 else total_things - 1
        
        start = self.last_file_index if self.last_file_index is not None else general_last_file_index
        
        for idx in range(start, -1, -2):
            file = self.things[idx]
            if file.size >= 1:
                self.last_file_index = idx
                return
        
        raise ValueError('No more files')
    
    def arranged_properly(self):
        self.calculate_empty_space_index()
        self.calculate_last_file_index()

        last_free_space = self.last_file_index - 1

        for idx in range(last_free_space, -1, -2):
            free_space = self.things[idx]
            if free_space.space >= 1:
                return False
            
        return True
    
    def checksum(self):
        result = 0

        idx = 0

        for thing in self.things:
            if type(thing) is File:
                for n in range(thing.size):
                    result += thing.id * idx
                    idx += 1
            elif type(thing) is FreeSpace:
                for file in thing.files.values():
                    for n in range(file.size):
                        result += file.id * idx
                        idx += 1

        return result

    def __str__(self):
        return format(self, 'l')
    
    def __format__(self, format_spec):
        match format_spec:
            case 's':
                return ''.join(f'{t:s}' for t in self.things)
            case 'l':
                other = f'empty_space_index={self.empty_space_index}, last_file_index={self.last_file_index}'
                return other + '\n' + '\n'.join(map(str, self.things))
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
    disk.calculate_empty_space_index()
    disk.calculate_last_file_index()

    # print(f'{disk:l}')
    # print(f'{disk:s}')

    while not disk.arranged_properly():
        free_space: FreeSpace = disk.things[disk.empty_space_index]
        if free_space.space <= 0:
            disk.calculate_empty_space_index()
            free_space: FreeSpace = disk.things[disk.empty_space_index]

        file: File = disk.things[disk.last_file_index]
        if file.size <= 0:
            disk.calculate_last_file_index()
            file: File = disk.things[disk.last_file_index]

        free_space.add_file(file)

        # print(f'{disk:s}')
    
    print(disk.checksum())


if __name__ == "__main__":
    main()
