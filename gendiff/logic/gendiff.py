import os.path
from gendiff.logic.data_parser import parse_to_dict

INDENT_CHAR = ' '
INDENT_REPEAT = 2


def get_data(file_path):
    DATA_TYPES = {
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml'
    }
    data_type = DATA_TYPES.get(os.path.splitext(file_path)[-1])
    # if data_type is None:
    #     return {}
    with open(file_path) as input_file:
        return parse_to_dict(input_file, data_type)


def generate_diff(file_path1, file_path2):
    f1 = get_data(file_path1)
    f2 = get_data(file_path2)
    keys_superset = set(f1.keys()) | set(f2.keys())
    result = '{\n'
    for key in sorted(keys_superset):
        indent = INDENT_CHAR * INDENT_REPEAT
        # ' ' for same value, '-' for any difference
        sign1 = ' ' if f1.get(key) == f2.get(key) else '-'
        # don't show in results for same value, '+' for any difference
        sign2 = '+'
        # it's in f1, show always
        if key in f1:
            result += f'{indent}{sign1} {key}: {bool_to_str(f1[key])}\n'
        # it's in f2, only show if the values differ
        if key in f2 and f1.get(key) != f2.get(key):
            result += f'{indent}{sign2} {key}: {bool_to_str(f2[key])}\n'
    result += '}'
    return result


def bool_to_str(value):
    # 'True' and 'False' must be lower case in output
    return str(value).lower() if isinstance(value, bool) else value
