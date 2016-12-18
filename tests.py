import utilities as ut
import unittest

class TestPopulationInitialization(unittest.TestCase):

    def test_uniform_float(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_uniform_categorical(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
