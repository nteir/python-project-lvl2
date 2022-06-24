import pytest
from gendiff import generate_diff

TEST_PARAMETERS = [
    (
        './tests/fixtures/flat_file1.json',
        './tests/fixtures/flat_file2.json',
        './tests/fixtures/flat_expected.txt',
        None,
    ),
    (
        './tests/fixtures/flat_file1.yml',
        './tests/fixtures/flat_file2.yml',
        './tests/fixtures/flat_expected.txt',
        None,
    ),
    (
        './tests/fixtures/nested_file1.json',
        './tests/fixtures/nested_file2.json',
        './tests/fixtures/nested_expected.txt',
        None,
    ),
    (
        './tests/fixtures/nested_file1.yml',
        './tests/fixtures/nested_file2.yml',
        './tests/fixtures/nested_expected.txt',
        None,
    ),
    (
        './tests/fixtures/nested_file1.json',
        './tests/fixtures/nested_file2.json',
        './tests/fixtures/format2_expected.txt',
        'plain',
    ),
    (
        './tests/fixtures/nested_file1.yml',
        './tests/fixtures/nested_file2.yml',
        './tests/fixtures/format2_expected.txt',
        'plain',
    ),
    (
        './tests/fixtures/nested_file1.json',
        './tests/fixtures/nested_file2.json',
        './tests/fixtures/format3_expected.txt',
        'json',
    ),
    (
        './tests/fixtures/nested_file1.yml',
        './tests/fixtures/nested_file2.yml',
        './tests/fixtures/format3_expected.txt',
        'json',
    ),
]


@pytest.fixture(name="test_params", params=TEST_PARAMETERS)
def _test_params(request):
    return request.param


def test_generate_diff(test_params):
    file1, file2, path_expected, format = test_params
    if format is None:
        recieved = generate_diff(file1, file2)
    else:
        recieved = generate_diff(file1, file2, format=format)
    expected = open(path_expected).read()
    assert recieved == expected
