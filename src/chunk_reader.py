CHUNK_SIZE = 2
INPUT_PATH = 'input.txt'
STOP_WORDS_PATH = 'stop_words.txt'

chunk = list[str]
stop_words = list[str]

def reader(path):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def create_chunks(lines):
    chunks = []
    for i in range(0, len(lines), CHUNK_SIZE):
        chunks.append(lines[i:i + CHUNK_SIZE])
    
    if chunks: return chunks
    else: return None

def init_chunks():
    lines = reader(INPUT_PATH)
    chunks = create_chunks(lines)
    if chunks: return chunks
    else: raise ValueError("Falha em iniciar os Chunks")

def init_stop_words():
    stop_words = reader(STOP_WORDS_PATH)
    if stop_words: return stop_words
    else: raise ValueError("Falha em iniciar as Stop Words")