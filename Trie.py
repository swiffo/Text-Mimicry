import random

class Trie:
    '''
    A light-weight trie (or prefix tree).
    '''

    def __init__(self):
        # The following lists must have the same lengths at all times. The elements are linked by index across
        # the lists. E.g., if _letters[2] == 'k', we find in _children[2] the trie with prefixes following the
        # letter 'k'. _counts[2] will be the number of times 'k' has occurred as part of a prefix.
        self._children = []  # List of trie's
        self._letters = []  # List of unique letters
        self._counts = []  # List of number of times a given letter has occurred as a prefix

    def add_word(self, word):
        '''Add word to the prefix tree.'''

        if not word:
            return

        letter = word[0]
        if letter in self._letters:
            index = self._letters.index(letter)
        else:
            self._children.append(Trie())
            self._letters.append(letter)
            self._counts.append(0)
            index = len(self._children) - 1

        self._counts[index] += 1
        next_node = self._children[index]
        next_node.add_word(word[1:])

    def total_count(self):
        '''Number of words that exist in the trie'''
        return sum(self._counts)

    def random_word(self, word_length, prefix=''):
        '''Return a random word from the prefix tree of specified length.

        Optionally specify a prefix to limit the selection space. Probability of a word being
        chosen is proportional to the number of times it has been added to the trie.

        Returns a string if successful. None if not possible to return a word within the constraints.
        '''
        if not word_length:
            return ''

        if prefix:
            if len(prefix) > word_length:
                return None

            letter = prefix[0]
            if letter not in self._letters:
                return None
            else:
                next_node = self._children[self._letters.index(letter)]
                remaining_word = next_node.random_word(word_length - 1, prefix[1:])
                if remaining_word is not None:
                    return letter + remaining_word
                else:
                    return None
        else:
            total_count = self.total_count()
            if not total_count:
                return None
            else:
                count_stop = random.randint(0, total_count - 1)
                index = -1
                while count_stop >= 0:
                    index += 1
                    count_stop -= self._counts[index]

                letter = self._letters[index]
                next_node = self._children[index]
                remaining_word = next_node.random_word(word_length - 1)
                if remaining_word is not None:
                    return letter + remaining_word
                else:
                    return None

    def random_text(self, word_length, max_text_length):
        '''Return randomised text by sequentially building words of length word_length.'''
        last_word = self.random_word(word_length)
        letters = list(last_word)[:-1]
        max_text_length -= len(letters)

        while last_word is not None and max_text_length > 0:
            letters.append(last_word[-1])
            max_text_length -= 1

            last_word = self.random_word(word_length, prefix=last_word[1:])

        return ''.join(letters)


    def feed_text(self, text, word_length):
        '''Add a word to the trie for every substring of text of length word_length.'''
        for start_index in range(len(text) - word_length + 1):
            self.add_word(text[start_index:start_index+word_length])