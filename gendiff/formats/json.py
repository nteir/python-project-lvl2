import json


def format(node):
    return json.dumps(node, sort_keys=True, indent=2)
