import pytest
from main import read_file, process_text, write_results

@pytest.fixture
def sample_text():
    return "the cat and the dog and the mouse"

@pytest.mark.parametrize("file_content, expected", [
    ("test test word", "test test word"),
    ("hello world", "hello world"),
])
def test_read_file(tmp_path, file_content, expected):
    file = tmp_path / "test.txt"
    file.write_text(file_content)
    assert read_file(str(file)) == expected

def test_process_text(sample_text):
    result = process_text(sample_text)
    assert len(result) <= 10
    assert result[0][0] == "the"  # "the" should be most frequent
    assert result[0][1] == 3      # "the" appears 3 times

def test_write_results(tmp_path):
    results = [("test", 5), ("word", 3)]
    output = tmp_path / "output.txt"
    write_results(results, str(output))
    with open(output, 'r') as f:
        content = f.read()
    assert content == "test-5\nword-3\n"