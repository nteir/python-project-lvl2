from gendiff.logic.data_parser import get_data_from_file
import gendiff.logic.generator
from gendiff.formats import FORMATS


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = get_data_from_file(file_path1)
    data2 = get_data_from_file(file_path2)
    diff = gendiff.logic.generator.generate_internal_diff(data1, data2)
    diff_string = FORMATS[format].format(diff)
    diff_string = diff_string.strip()
    return diff_string
