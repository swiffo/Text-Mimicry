import random

class Trie:
    """A light-weight trie (or prefix tree)."""

    def __init__(self):
        """Initialise Trie()."""
        # The following lists must have the same lengths at all times. The elements are linked by index across
        # the lists. E.g., if _letters[2] == 'k', we find in _children[2] the trie with prefixes following the
        # letter 'k'. _counts[2] will be the number of times 'k' has occurred as part of a prefix.
        self._children = []  # List of trie's
        self._letters = []  # List of unique letters
        self._counts = []  # List of number of times a given letter has occurred as a prefix

    def add_word(self, word):
        """Adds word to the prefix tree.

        Args:
            word: Word (string) to add to the trie.

        Returns:
            None
        """
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
        """Returns the count of words added to the trie.

        Note that duplicates are counted.
        """
        return sum(self._counts)

    def random_word(self, word_length, prefix=''):
        """Returns a random word from the trie.

        The word returned is chosen with probability proportional to the number of times
        such a word has been added to the trie. A prefix can optionally be specified to
        limit the selection space.

        Args:
            word_length: Integer specifying the length of the random word to be generated.
            prefix: A string of length less than or equal to word_length which constrains
                the random word to be generated to start with the prefix.

        Returns:
            A word of length word_length chosen with probability proportional to the occurrence
            count in the trie.

            If it is not possible to form such a word (e.g., prefix too constraining or
            required length too long), None is returned.
        """
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
        """Returns randomised text.

        The text returned is built sequentially by first constructing a random
        word of length word_length and then inductively extending this by
        creating new random words of length word_length prefixed by the previous
        word_length-1 characters.

        Args:
            word_length: Length of the words used to inductively build the
                randomised text.
            max_text_length: The longest the randomised text is allowed to grow
                before being cut and returned.

        Returns:
            A string of length no greater than max_text_length. The string is a randomised
            text built based on the word occurrences in the trie. If at some point it
            is not possible to built the string further (the max length is reached or no
            word in the trie can extend the last word_length-1 characters), the string is
            returned as is.
        """
        last_word = self.random_word(word_length)
        letters = list(last_word)[:-1]
        max_text_length -= len(letters)

        while last_word is not None and max_text_length > 0:
            letters.append(last_word[-1])
            max_text_length -= 1

            last_word = self.random_word(word_length, prefix=last_word[1:])

        return ''.join(letters)


    def feed_text(self, text, word_length):
        """Adds words to the trie from the given text.

        Adds all substrings of length word_length from text to the trie.

        Args:
            text: A string from which to extract the words to add to the trie.
            word_length: The length of the substrings to be extracted from text.

        Returns:
            None.
        """
        for start_index in range(len(text) - word_length + 1):
            self.add_word(text[start_index:start_index+word_length])
