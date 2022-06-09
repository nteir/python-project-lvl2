from gendiff import generate_diff


def test_flat_json_generate_diff():
    file1 = './tests/fixtures/flat_file1.json'
    file2 = './tests/fixtures/flat_file2.json'
    recieved = generate_diff(file1, file2)
    expected = open('./tests/fixtures/flat_expected.txt').read()
    assert recieved == expected


def test_flat_yaml_generate_diff():
    file1 = './tests/fixtures/flat_file1.yml'
    file2 = './tests/fixtures/flat_file2.yml'
    recieved = generate_diff(file1, file2)
    expected = open('./tests/fixtures/flat_expected.txt').read()
    assert recieved == expected


def test_nested_json_generate_diff():
    file1 = './tests/fixtures/nested_file1.json'
    file2 = './tests/fixtures/nested_file2.json'
    recieved = generate_diff(file1, file2)
    expected = open('./tests/fixtures/nested_expected.txt').read()
    assert recieved == expected


def test_nested_yaml_generate_diff():
    file1 = './tests/fixtures/nested_file1.yml'
    file2 = './tests/fixtures/nested_file2.yml'
    recieved = generate_diff(file1, file2)
    expected = open('./tests/fixtures/nested_expected.txt').read()
    assert recieved == expected
