import pytest
import src.kwic as kwic
import src.chunk_reader as reader

TEST_PATH = "tests/input_example/input_test"

def path(n):
    return TEST_PATH+str(n)+'.txt'

def test_kwic_chunk():
    stop_words = ["a", "o", "um"]
    

def test_kwic_chunk_example():
    stop_words = ["the", "is", "sat","a"]
    lines = reader.reader(path(4))
    assert kwic.kwic_chunk(stop_words,lines ) == [
        ('brown','brown cat sat A' ,'A brown cat sat'),
        ('brown','brown fox The quick' ,'The quick brown fox'),
        ('brown','brown The cat is' ,'The cat is brown'),
        ('cat','cat is brown The' ,'The cat is brown'),
        ('cat','cat sat A brown' ,'A brown cat sat'),
        ('fox','fox The quick brown' ,'The quick brown fox'),
        ('quick','quick brown fox The' ,'The quick brown fox')
        ]


