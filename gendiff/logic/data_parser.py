import json
import yaml


def parse_to_dict(data, data_type):
    PARSING_FUNC = {
        'json': json.load,
        'yaml': lambda data: yaml.load(data, Loader = yaml.Loader),
    }
    if data_type in PARSING_FUNC:
        return PARSING_FUNC[data_type](data)
    else:
        return {}
