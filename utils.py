import re
import requests

import Trie

GUTENBERG_END = 'End of the Project Gutenberg EBook'

def add_from_text(text, word_length, trie=None):
    '''Add all substrings from text with length word_length to the trie.

    If no trie is specified, an empty one is first created.
    '''
    if trie is None:
        trie = Trie.Trie()

    trie.feed_text(text, word_length)

    return trie

def clean_gutenberg_txt(raw_text):
    '''
    Remove pre- and post-amble from Gutenberg texts and convert carriage returns
    into single whitespace.
    '''
    if len(raw_text) < 11000:
        return ''

    start_index = raw_text.index('. ', 10000) + 2  # No error handling!!
    try:
        end_index = raw_text.index(GUTENBERG_END, start_index)
    except ValueError:
        end_index = None

    text = raw_text[start_index:end_index]
    text.replace(r'\r\n', ' ')

    whitespace_pattern = re.compile(r'\s+')
    text = whitespace_pattern.sub(' ', text)

    return text


def add_from_gutenberg(urls, word_length, trie=None):
    '''
    Add all substring from the Gutenberg text of length word_length to the trie.

    If no trie is specified, create an empty one first.

    :param urls:
    :param word_length:
    :param trie:
    :return: Trie
    '''
    if trie is None:
        trie = Trie.Trie()

    for url in urls:
        print(url)
        response = requests.get(url)
        print('!!!! length = {}'.format(len(response.text)))
        text = clean_gutenberg_txt(response.text)
        trie.feed_text(text, word_length)

    return trie