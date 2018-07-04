import utils

def speak_Shakespearean():
    '''Create trie from Shakespeare texts and print some randomly generated texts.'''
    shakespeare_urls = [
        'http://www.gutenberg.org/cache/epub/2264/pg2264.txt', # Macbeth
        'https://www.gutenberg.org/files/1524/1524-0.txt',  # Hamlet
        'http://www.gutenberg.org/cache/epub/2243/pg2243.txt'  # Merchant of Venice
    ]

    for word_length in [3, 5, 10]:
        print('*** WORD LENGTH {}'.format(word_length))
        trie = utils.add_from_gutenberg(shakespeare_urls, word_length)
        text = trie.random_text(word_length, 500)

        try:
            possible_start_index = text.index('. ')
        except ValueError:
            possible_start_index = None

        if possible_start_index is not None and possible_start_index < 100:
            text = text[possible_start_index + 2:]

        print(text)


if __name__ == '__main__':
    speak_Shakespearean()