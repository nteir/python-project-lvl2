

def format(node, path=''):
    result = ''
    for key, val in sorted(node.items()):
        node_type = val.get('type')
        new_path = f"{path}.{key}" if path else key
        if node_type == 'parent':
            value = val.get('value')
            result += format(value, path=new_path)
        if node_type in ['removed', 'added', 'changed']:
            value1 = val.get('value')
            value1 = val.get('value1') if value1 is None else value1
            value2 = val.get('value2')
            result += get_value_string(node_type, new_path, value1, value2)
    return result


def get_value_string(node_type, path, value1, value2=None):
    result = f"Property '{path}' was "
    if node_type == 'removed':
        result += 'removed\n'
    elif node_type == 'added':
        val = cast_type(value1)
        result += f"added with value: {val}\n"
    elif node_type == 'changed':
        val1 = cast_type(value1)
        val2 = cast_type(value2)
        result += f"updated. From {val1} to {val2}\n"
    return result


def cast_type(value):
    if isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    elif isinstance(value, dict):
        result = '[complex value]'
    else:
        result = f"'{value}'"
    return result
