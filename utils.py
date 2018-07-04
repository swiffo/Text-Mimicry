import re

import requests

import Trie

_GUTENBERG_END = 'End of the Project Gutenberg EBook'

def add_from_text(text, word_length, trie=None):
    """Adds all substrings of text with specified length to a trie.

    If no trie is specified, an empty one is first created.

    Args:
        text: A string from which the words to add to the trie are formed.
        word_length: Integer specifying length of the substrings of text.
        trie: A trie (Trie.Trie). Optional. If not specified an empty one is created.

    Returns:
        A trie (Trie.Trie).
    """
    if trie is None:
        trie = Trie.Trie()

    trie.feed_text(text, word_length)

    return trie

def clean_gutenberg_txt(raw_text):
    """Cleans text string from Gutenberg project.

    Takes a Project Gutenberg text as string and attempts removing pre- and post-amble.
    Also converts line breaks into whitespace.

    Args:
        raw_text: Full text (string) of a Project Gutenberg book.

    Returns:
         A string.
    """
    if len(raw_text) < 11000:
        return ''

    start_index = raw_text.index('. ', 10000) + 2  # No error handling!!
    try:
        end_index = raw_text.index(_GUTENBERG_END, start_index)
    except ValueError:
        end_index = None

    text = raw_text[start_index:end_index]
    text.replace(r'\r\n', ' ')

    whitespace_pattern = re.compile(r'\s+')
    text = whitespace_pattern.sub(' ', text)

    return text


def add_from_gutenberg(urls, word_length, trie=None):
    """Adds substrings from Project Gutenberg text to a trie.

    Takes URLs for a Project Gutenberg book and adds all substrings of length
    word_length from those texts to a trie. If no trie is supplied, a new one is created.

    Args:
        urls: A list of URLs to Project Gutenberg text files.
        word_length: Integer specifying the length of the substrings to add to the trie.
        trie: Optional. A trie (Trie.Trie). If not supplied, an empty trie will be created.

    Returns:
        A trie (Trie.Trie).
    """
    if trie is None:
        trie = Trie.Trie()

    for url in urls:
        response = requests.get(url)
        text = clean_gutenberg_txt(response.text)
        trie.feed_text(text, word_length)

    return trie
