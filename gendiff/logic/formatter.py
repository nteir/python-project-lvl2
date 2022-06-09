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


def stylish(diff):
    diff_string = ""
    def build_node_string(node, deapth=0):
        indent_count = STYLISH_CONST['indent_initial'] + STYLISH_CONST['indent_repeat'] * deapth
        indent = STYLISH_CONST['indent_char'] * indent_count
        indent_count = STYLISH_CONST['indent_repeat'] * deapth
        indent2 = STYLISH_CONST['indent_char'] * indent_count
        res = "{\n"
        for key, val in sorted(node.items()):
            strings = ''
            if isinstance(val, dict):
                node_type = val['type']
                if node_type == 'unchanged':
                    value = build_node_string(val['value'], deapth+1) if isinstance(val['value'], dict) else cast_type(val['value'])
                    strings = f"{indent}{STYLISH_CONST['unchanged']} {key}: {value}\n"
                elif node_type == 'changed':
                    value1 = build_node_string(val['value1'], deapth+1) if isinstance(val['value1'], dict) else cast_type(val['value1'])
                    value2 = build_node_string(val['value2'], deapth+1) if isinstance(val['value2'], dict) else cast_type(val['value2'])
                    strings = f"{indent}{STYLISH_CONST['removed']} {key}: {value1}\n"
                    strings += f"{indent}{STYLISH_CONST['added']} {key}: {value2}\n"
                elif node_type == 'removed':
                    value = build_node_string(val['value'], deapth+1) if isinstance(val['value'], dict) else cast_type(val['value'])
                    strings = f"{indent}{STYLISH_CONST['removed']} {key}: {value}\n"
                elif node_type == 'added':
                    value = build_node_string(val['value'], deapth+1) if isinstance(val['value'], dict) else cast_type(val['value'])
                    strings = f"{indent}{STYLISH_CONST['added']} {key}: {value}\n"
                elif node_type == 'parent':
                    value = build_node_string(val['value'], deapth+1)
                    strings = f"{indent}{STYLISH_CONST['parent']} {key}: {value}\n"
            res += strings
        res += f'{indent2}}}'
        return res
    diff_string = build_node_string(diff)
    return diff_string


def cast_type(value):
    if isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    else:
        result = str(value)
    return result
