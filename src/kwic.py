import re
from typing import TypeAlias
from itertools import chain

Kwic_format: TypeAlias = tuple[str,str,str]

def kwic_line(line, stop_words)->list[tuple[str,str,str]]:
    # Extract keywords and generate shifted lines
    results = []
    words = re.findall(r'\b\w+\b', line)
    for i, word in enumerate(words):
        if word.lower() not in stop_words:
            # Create circular shift
            shifted = ' '.join(words[i:] + words[:i])
            results.append(
                (word.lower(), shifted, line)
            )
    return sorted(results, key=lambda x: (x[0].lower(), x[1].lower()))

def kwic_chunk(chunk, stop_words)->list[tuple[str,str,str]]:
    return sorted(chain.from_iterable(kwic_line(line, stop_words) for line in chunk),key=lambda x: (x[0].lower(), x[1].lower()))


stop_words = ["stop", "words", "personalizado"]
print(kwic_line("Stop, WORDS, PERSONALIZADO, A o e i u", stop_words))