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

    def build_node_string(node, deapth=0):
        indent_count = STYLISH_CONST['indent_repeat'] * deapth
        indent = STYLISH_CONST['indent_char'] * indent_count
        res = "{\n"
        for key, val in sorted(node.items()):
            strings = ''
            if isinstance(val, dict):
                node_type = val['type']
                if node_type == 'changed':
                    value = build_node_string(
                        val['value1'], deapth + 1
                    ) if isinstance(val['value1'], dict) else val['value1']
                    strings = get_node_string('removed', key, value, deapth)
                    value = build_node_string(
                        val['value2'], deapth + 1
                    ) if isinstance(val['value2'], dict) else val['value2']
                    strings += get_node_string('added', key, value, deapth)
                else:
                    value = build_node_string(
                        val['value'], deapth + 1
                    ) if isinstance(val['value'], dict) else val['value']
                    strings = get_node_string(node_type, key, value, deapth)
            res += strings
        res += f'{indent}}}'
        return res
    diff_string = build_node_string(diff)
    return diff_string


def get_node_string(node_type, key, value, deapth=0):
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
