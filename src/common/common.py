import inspect
import os


def __get_caller_frame():
    frames = inspect.stack()

    current_frame = inspect.stack()[0]
    for frame in frames[1:]:
        if frame.filename != current_frame.filename:
            return frame


def __get_caller_file_path():
    caller_frame = __get_caller_frame()
    caller_file_path = caller_frame.filename

    caller_file_path = os.path.dirname(caller_file_path)

    return caller_file_path


def __strip(line):
    return line.strip()


def get_lines(suffix=''):
    file_path = __get_caller_file_path()
    with open(f'{file_path}/in{suffix}.txt') as f:
        return list(map(__strip, f.readlines()))
