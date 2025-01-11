import pytest
import src.chunk_reader as reader
import src.kwic as kwic
from functools import partial
from itertools import chain

TEST_PATH = "tests/input_example/input_test"

def path(n):
    return TEST_PATH+str(n)+'.txt'

def test_kwic_map():
    stop_words = ["the", "is", "sat","a"]
    reader.INPUT_PATH = path(4)
    chunks = [['The quick brown fox', 'A brown cat sat'], ['The cat is brown']]
    kwic_chunk_partial = partial(kwic.kwic_chunk,stop_words)
    x =  sorted(chain.from_iterable(list(map(kwic_chunk_partial,(chunks)))),key=lambda x: (x[0].lower(), x[1].lower()))
    assert x == [
        ('brown','brown cat sat A' ,'A brown cat sat'),
        ('brown','brown fox The quick' ,'The quick brown fox'),
        ('brown','brown The cat is' ,'The cat is brown'),
        ('cat','cat is brown The' ,'The cat is brown'),
        ('cat','cat sat A brown' ,'A brown cat sat'),
        ('fox','fox The quick brown' ,'The quick brown fox'),
        ('quick','quick brown fox The' ,'The quick brown fox')
        ]


def test_kwic_threads():
    stop_words = ["the", "is", "sat","a"]
    reader.INPUT_PATH = path(4)
    chunks = reader.init_chunks()
    assert kwic.kwic_threads(stop_words,chunks) == [
        ('brown','brown cat sat A' ,'A brown cat sat'),
        ('brown','brown fox The quick' ,'The quick brown fox'),
        ('brown','brown The cat is' ,'The cat is brown'),
        ('cat','cat is brown The' ,'The cat is brown'),
        ('cat','cat sat A brown' ,'A brown cat sat'),
        ('fox','fox The quick brown' ,'The quick brown fox'),
        ('quick','quick brown fox The' ,'The quick brown fox')
        ]