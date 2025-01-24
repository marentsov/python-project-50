import pytest

from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.parser import parse_data_from_file, read_file


@pytest.mark.parametrize('file_path1, file_path2, expected_result', [
    ("tests/test_data/file1.json",
     'tests/test_data/file2.json',
     'tests/test_data/expected_result_json.txt')])
def test_generate_diff(file_path1, file_path2, expected_result):
    file1 = parse_data_from_file(file_path1)
    file2 = parse_data_from_file(file_path2)
    diff = generate_diff(file1, file2)
    expected = read_file(expected_result)
    assert diff == expected






