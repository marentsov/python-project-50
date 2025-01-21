import json


def parse_file(file_path):
    with open(file_path, 'r') as file:
        return json.loads(file.read())



def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


def generate_diff(file1, file2):
    result_file = ''
    for i in sorted(file1):
        if i not in file2:
            result_file += f' - {i}: {format_value(file1[i])}\n'
        elif (i in file2) and (file1[i] == file2[i]):
            result_file += f'   {i}: {format_value(file1[i])}\n'
        elif (i in file2) and (file1[i] != file2[i]):
            result_file += f' - {i}: {format_value(file1[i])}\n'
            result_file += f' + {i}: {format_value(file2[i])}\n'

    file3 = {key: value for key, value in file2.items() if key not in file1}
    if len(file3) != 0:
        for i in file3:
            result_file += f' + {i}: {format_value(file2[i])}\n'

    result = '{\n' + result_file + '}'
    return result


