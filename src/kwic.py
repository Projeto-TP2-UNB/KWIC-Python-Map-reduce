import re
from typing import TypeAlias
from itertools import chain
from functools import partial
import concurrent.futures

Kwic_format: TypeAlias = tuple[str,str,str]

def kwic_line(stop_words,line)->list[tuple[str,str,str]]:
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

def kwic_chunk(stop_words,chunk)->list[tuple[str,str,str]]:
    return sorted(chain.from_iterable(kwic_line(stop_words,line) for line in chunk),key=lambda x: (x[0].lower(), x[1].lower()))

def kwic_threads(stop_words, chunks):
    kwic_chunk_partial = partial(kwic_chunk,stop_words)
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit tasks to the pool
        futures = {executor.submit(kwic_chunk_partial, item): item for item in chunks}
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(futures):
            result = future.result()  # Get the result of the computation
            results.append(result)
    
    return sorted(chain.from_iterable(results),key=lambda x: (x[0].lower(), x[1].lower()))
