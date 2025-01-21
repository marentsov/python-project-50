from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.generate_diff import parse_file
from gendiff.scripts.generate_diff import format_value


def find_diff(file_path1, file_path2):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)

    diff = generate_diff()

    return diff




