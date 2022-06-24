from gendiff.formats import stylish, plain, json

__all__ = ('stylish', 'plain', 'json')

FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}
