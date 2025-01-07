import re

def kwic_line(line, stop_words):
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
    return results

def kwic_chunk(chunk, stop_words):
    return [kwic_line(line, stop_words) for line in chunk]

stop_words = ["stop", "words", "personalizado"]
print(kwic_line("Stop, WORDS, PERSONALIZADO, A o e i u", stop_words))