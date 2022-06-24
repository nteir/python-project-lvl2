STYLISH_CONST = {
    'indent_char': ' ',
    'indent_initial': 2,
    'indent_repeat': 4,
    'unchanged': ' ',
    'changed': ' ',
    'parent': ' ',
    'removed': '-',
    'added': '+'
}


def format(data):
    def go_deeper(node, deapth=0):
        indent_count = STYLISH_CONST['indent_repeat'] * deapth
        indent = STYLISH_CONST['indent_char'] * indent_count
        result = "{\n"
        for key, val in sorted(node.items()):
            node_type = val.get('type')
            if node_type == 'parent':
                value = val.get('value')    # is dict, has type
                value = go_deeper(value, deapth + 1)
                result += get_value_string(node_type, key, value, deapth)
            elif node_type == 'changed':
                value = stringify_dict(val.get('value1'), deapth)
                result += get_value_string('removed', key, value, deapth)
                value = stringify_dict(val.get('value2'), deapth)
                result += get_value_string('added', key, value, deapth)
            else:
                value = stringify_dict(val.get('value'), deapth)
                result += get_value_string(node_type, key, value, deapth)
        result += f'{indent}}}'
        return result
    return go_deeper(data)


def stringify_dict(data, deapth):
    if not isinstance(data, dict):
        return data
    indent_count = STYLISH_CONST['indent_repeat'] * (deapth + 1)
    indent = STYLISH_CONST['indent_char'] * indent_count
    result = '{\n'
    for key, val in data.items():
        if isinstance(val, dict):
            strings = stringify_dict(val, deapth + 1)
        else:
            strings = val
        result += get_value_string('unchanged', key, strings, deapth + 1)
    result += f'{indent}}}'
    return result


def get_value_string(node_type, key, value, deapth=0):
    indent_count = STYLISH_CONST['indent_repeat'] * deapth
    indent_count = STYLISH_CONST['indent_initial'] + indent_count
    indent = STYLISH_CONST['indent_char'] * indent_count
    if not isinstance(value, dict):
        value = cast_type(value)
    return f"{indent}{STYLISH_CONST[node_type]} {key}: {value}\n"


def cast_type(value):
    if isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    else:
        result = str(value)
    return result
