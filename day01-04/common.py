import inspect
import os
import re


def get_caller_frame():
    frames = inspect.stack()

    current_frame = inspect.stack()[0]
    for frame in frames[1:]:
        if frame.filename != current_frame.filename:
            return frame


def get_caller_filename():
    caller_frame = get_caller_frame()
    caller_filename = caller_frame.filename

    filename = os.path.splitext(os.path.basename(caller_filename))[0]

    return filename

def clean_caller_filename():
    filename = get_caller_filename()

    regex = re.compile(r"(.+)\s+\(part \d+\)")

    return regex.search(filename).group(1)


def strip(line):
    return line.strip()


def get_lines():
    filename = clean_caller_filename()
    with open(f'{filename}.in.txt') as f:
        return list(map(strip, f.readlines()))
