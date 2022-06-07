from gendiff import generate_diff


def test_flat_generate_diff():
    file1 = './tests/fixtures/flat_file1.json'
    file2 = './tests/fixtures/flat_file2.json'
    recieved = generate_diff(file1, file2)
    expected = open('./tests/fixtures/flat_expected.txt').read()
    assert recieved == expected
