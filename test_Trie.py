import unittest

import Trie

class TestTrie(unittest.TestCase):
    def test_total_count(self):
        t = Trie.Trie()
        self.assertEqual(t.total_count(), 0)

        t.add_word('wonder')
        t.add_word('happy')
        t.add_word('beautiful')

        self.assertEqual(t.total_count(), 3)

        t.add_word('')
        self.assertEqual(t.total_count(), 3)

    def test_random_word(self):
        t = Trie.Trie()
        t.add_word('wonky')

        random_word = t.random_word(3)
        self.assertIsInstance(random_word, str)
        self.assertEqual(len(random_word), 3)

        self.assertIsNone(t.random_word(100))

        t.add_word('toaster')
        t.add_word('care bear')
        t.add_word('croakamancer')

        prefix = 'toa'
        for counter in range(10):
            prefixed_word = t.random_word(5, prefix=prefix)
            self.assertSequenceEqual(prefixed_word[:len(prefix)], prefix, seq_type=str)


if __name__ == '__main__':
    unittest.main()