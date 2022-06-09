

def generate_node(data1, data2, key, parent_flag=False):
    node = {}
    value1 = data1.get(key)
    value2 = data2.get(key)
    if parent_flag == True:
        node['type'] = 'unchanged'
        node['value'] = generate_internal_diff(value1, {}, parent_flag=True) if isinstance(value1, dict) else value1
    else:
        if key in data1 and key in data2:
            if isinstance(value1, dict) and isinstance(value2, dict):
                node['type'] = 'parent'
                node['value'] = generate_internal_diff(value1, value2)
            elif value1 == value2:
                node['type'] = 'unchanged'
                node['value'] = value1
            else:
                node['type'] = 'changed'
                node['value1'] = generate_internal_diff(value1, {}, parent_flag=True) if isinstance(value1, dict) else value1
                node['value2'] = generate_internal_diff(value2, {}, parent_flag=True) if isinstance(value2, dict) else value2
        elif key in data1:
            node['type'] = 'removed'
            node['value'] = generate_internal_diff(value1, {}, parent_flag=True) if isinstance(value1, dict) else value1
        elif key in data2:
            node['type'] = 'added'
            node['value'] = generate_internal_diff(value2, {}, parent_flag=True) if isinstance(value2, dict) else value2
    return node


def generate_internal_diff(data1, data2, parent_flag=False):
    key_list = data1.keys() | data2.keys()
    diff = {key: generate_node(data1, data2, key, parent_flag) for key in key_list}
    return diff
