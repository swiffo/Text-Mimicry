import unittest

import Trie
import utils


class TestUtils(unittest.TestCase):
    def test_add_from_test(self):
        text = 'It was an itsy-bitsy, teeny-weenie'
        word_length = 4
        t = utils.add_from_text(text, word_length)

        self.assertEqual(t.total_count(), len(text) + 1 - word_length)

    def test_clean_gutenberg_text(self):
        gutenberg_txt = (r'panion was a terrier, with whom\r\nhe would play all sorts of tricks'
                         + r'--tumbling and rolling over the\r\nanimal in the most amusing manner,'
                         + r' without hurting it. He would\r\nalso frequently run out on the bowsprit,'
                         + r'and climb about the\r\nrigging with the agility of a cat.\r\n\r\nOn his arrival'
                         + r'in England, he was sent to the menagerie at the\r\nTower. While there, another'
                         + r'terrier was introduced into his den.\r\nPossibly he may have mistaken it for his'
                         + r'old friend, for he\r\nimmediately became attached to the dog, and a')

        self.assertIn(r'\r\n', gutenberg_txt)
        clean_txt = utils.clean_gutenberg_txt(gutenberg_txt)
        self.assertNotIn(r'\r\n', clean_txt)

    def test_add_from_gutenberg(self):
        jungle_book_url = 'https://www.gutenberg.org/files/236/236-0.txt'

        t = utils.add_from_gutenberg(jungle_book_url, 4)
        self.assertIsInstance(t, Trie.Trie)


if __name__ == '__main__':
    unittest.main()