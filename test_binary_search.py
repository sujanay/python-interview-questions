import unittest
from binary_search import randomListGenerator

class TestBinarySearch(unittest.TestCase):
    def test_random(self):
        # Test random num list when size < 0
        self.assertRaises(TypeError, randomListGenerator, )