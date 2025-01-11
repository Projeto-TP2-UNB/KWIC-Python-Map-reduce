import pytest
import src.kwic as kwic


def test_kwic_line():
    stop_words = ["o", "a", "e"]
    assert kwic.kwic_line(stop_words,"O cabral a beijou") == [
        ('beijou', 'beijou O cabral a', 'O cabral a beijou'),
        ('cabral', 'cabral a beijou O', 'O cabral a beijou')
        
    ]

def test_kwic_line2():
    stop_words = ["stop", "words", "personalizado"]
    assert kwic.kwic_line(stop_words,"Stop, WORDS, PERSONALIZADO, A o e i u") == [
        ('a', 'A o e i u Stop WORDS PERSONALIZADO', 'Stop, WORDS, PERSONALIZADO, A o e i u'), 
        ('e', 'e i u Stop WORDS PERSONALIZADO A o', 'Stop, WORDS, PERSONALIZADO, A o e i u'),
        ('i', 'i u Stop WORDS PERSONALIZADO A o e', 'Stop, WORDS, PERSONALIZADO, A o e i u'),
        ('o', 'o e i u Stop WORDS PERSONALIZADO A', 'Stop, WORDS, PERSONALIZADO, A o e i u'), 
        ('u', 'u Stop WORDS PERSONALIZADO A o e i', 'Stop, WORDS, PERSONALIZADO, A o e i u')
    ]

