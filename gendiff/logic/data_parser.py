import json
import yaml
import os.path


def get_data_from_file(file_path):
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


def parse_to_dict(data, data_type):
    PARSING_FUNC = {
        'json': json.load,
        'yaml': lambda data: yaml.load(data, Loader=yaml.Loader)
    }
    if data_type in PARSING_FUNC:
        return PARSING_FUNC[data_type](data)
    else:
        raise TypeError('Unsupported data type')
