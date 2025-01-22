import pytest
from gendiff.scripts.generate_diff import generate_diff




@pytest.mark.parametrize('file1, file2, expected_result', [
    ("tests/test_data/file1.json",
     'tests/test_data/file2.json',
  'tests/test_data/expected_result_json.txt')])


def test_generate_diff(file1, file2, expected_result):
    diff = generate_diff(file1, file2)
    expected = read_file(expected_result)
    assert diff == expected


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()



