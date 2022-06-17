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
    if data_type is None:
        raise TypeError('Unsupported file format')
    with open(file_path) as input_file:
        return parse_to_dict(input_file, data_type)


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = gendiff.logic.generator.generate_internal_diff(data1, data2)
    diff_string = FORMATS[format].format(diff)
    diff_string = diff_string.strip()
    return diff_string
