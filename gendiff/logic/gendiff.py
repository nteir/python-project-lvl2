import os.path
from gendiff.logic.data_parser import parse_to_dict
import gendiff.logic.generator
from gendiff.formats import stylish, plain, json

FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def get_data(file_path):
    DATA_TYPES = {
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml'
    }
    data_type = DATA_TYPES.get(os.path.splitext(file_path)[-1])
    with open(file_path) as input_file:
        return parse_to_dict(input_file, data_type)


def generate_diff(file_path1, file_path2, format='stylish'):
    f1 = get_data(file_path1)
    f2 = get_data(file_path2)
    diff = gendiff.logic.generator.generate_internal_diff(f1, f2)
    result = FORMATS[format].format(diff)
    result = result.strip()
    return result
