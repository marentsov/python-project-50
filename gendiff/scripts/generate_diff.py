
def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


def generate_diff(file1, file2):
    ADD = ' + '
    DEL = ' - '
    CON = '   '

    result_file = ""
    combined_file = file1 | file2

    for i in sorted(file1):
        if i not in file2:
            result_file += f'{DEL}{i}: {format_value(file1[i])}\n'
        elif (i in file2) and (file1[i] == file2[i]):
            result_file += f'{CON}{i}: {format_value(file1[i])}\n'
        elif (i in file2) and (file1[i] != file2[i]):
            result_file += f'{DEL}{i}: {format_value(file1[i])}\n'
            result_file += f'{ADD}{i}: {format_value(file2[i])}\n'
        elif (i in combined_file) and (i not in file1):
            result_file += f'{ADD}{i}: {format_value(file2[i])}\n'

    result = '{\n' + result_file + '}'
    return result







