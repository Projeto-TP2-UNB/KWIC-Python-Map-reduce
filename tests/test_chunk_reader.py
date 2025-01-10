import pytest
import src.chunk_reader as reader
TEST_PATH = "tests/input_example/input_test"

def path(n):
    return TEST_PATH+str(n)+'.txt'

def test_reader():
    print (reader.reader(path(1)))
    assert reader.reader(path(1)) == ['linha1', 'linha2', 'linha3']

def test_create_chunks():
    lines = reader.reader(path(1))
    assert reader.create_chunks(lines) == [['linha1', 'linha2'], ['linha3']]

def test_create_chunks2():
    lines = reader.reader(path(2))
    assert reader.create_chunks(lines) == [['linha1', 'linha2'], ['linha3', 'linha4'], ['linha5']]

def test_init_chunks_sad_path():
    reader.INPUT_PATH = path(3)
    with pytest.raises(ValueError) as excinfo:
        reader.init_chunks()
    assert excinfo.type is ValueError

def test_init_chunks_happy_path():
    reader.INPUT_PATH = path(1)
    assert reader.init_chunks() == [['linha1', 'linha2'], ['linha3']]

def test_init_stop_words_sad_path():
    reader.STOP_WORDS_PATH = path(3)
    with pytest.raises(ValueError) as excinfo:
        reader.init_stop_words()
    assert excinfo.type is ValueError

def test_init_stop_words_happy_path():
    reader.STOP_WORDS_PATH = path(1)
    assert reader.init_stop_words() == ['linha1', 'linha2', 'linha3']