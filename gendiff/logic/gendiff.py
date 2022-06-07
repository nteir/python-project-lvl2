# import os
import json

INDENT_CHAR = ' '
INDENT_REPEAT = 2


def generate_diff(file_path1, file_path2):
    # return os.getcwd()
    # return os.path.isfile(file_path1)
    f1 = json.load(open(file_path1))
    f2 = json.load(open(file_path2))
    keys_superset = set(f1.keys()) | set(f2.keys())
    result = '{\n'
    for key in sorted(keys_superset):
        indent = INDENT_CHAR * INDENT_REPEAT
        sign1 = ' ' if f1.get(key) == f2.get(key) else '-'    # ' ' for same value, '-' for any difference
        sign2 = '+'                                           # don't show in results for same value, '+' for any difference
        if key in f1:                                         # it's in f1, show always
            result += f'{indent}{sign1} {key}: {bool_to_str(f1[key])}\n'
        if key in f2 and f1.get(key) != f2.get(key):          # it's in f2, only show if the values differ
            result += f'{indent}{sign2} {key}: {bool_to_str(f2[key])}\n'
    result += '}'
    return result


def bool_to_str(value):
    # 'True' and 'False' must be lower case in output
    return str(value).lower() if isinstance(value, bool) else value
