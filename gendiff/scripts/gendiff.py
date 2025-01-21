import argparse
from gendiff.scripts.generate_diff import parse_file
from gendiff.scripts.generate_diff import format_value
from gendiff.scripts.generate_diff import generate_diff





def parser_function():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help='set format of output')



    return parser.parse_args()



def main():
    args = parser_function()

    file_path1 = args.first_file
    file_path2 = args.second_file

    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)


    diff = generate_diff(file1, file2)

    print(diff)



if __name__ == "__main__":
    main()
