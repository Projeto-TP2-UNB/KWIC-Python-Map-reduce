import kwic
import chunk_reader

def main():
    chunks = chunk_reader.init_chunks()
    stop_words = chunk_reader.init_stop_words()

    contextos = kwic.kwic_threads(stop_words, chunks)
    for palavra, contexto, origem in contextos:
        print(f'{palavra} - {contexto} - {origem}')

if __name__ == '__main__':
    main()