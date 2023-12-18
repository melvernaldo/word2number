from word2number import word2number
import unittest
import warnings

class TestWord2Number(unittest.TestCase):
    def test_with_worded_integers(self):
        self.assertEqual(word2number('Three hundred and twelve'), 312)
        self.assertEqual(word2number('twelve hundred'), 1200)
        self.assertEqual(word2number('ten thousand'), 10000)
    
    def test_with_worded_negative_integers(self):
        self.assertEqual(word2number('Negative three hundred and eleven'), -311)
        self.assertEqual(word2number('Negative twelve hundred'), -1200)
        self.assertEqual(word2number('negative ten thousand'), -10000)

    def test_capitalizations(self):
        self.assertEqual(word2number('ThrEE HunDrEd anD TWELVe'), 312)
        self.assertEqual(word2number('TeN ThoUsaNd'), 10000)

    def test_invalid_words_warning(self):
        self.assertWarns(RuntimeWarning, word2number, 'Three Ligmas')
        self.assertWarns(RuntimeWarning, word2number, 'YOLO')
        self.assertWarns(RuntimeWarning, word2number, 'Teen thousand')
        
    def test_invalid_type(self):
        self.assertRaises(TypeError, word2number, 2000)
        self.assertRaises(TypeError, word2number, [1, 2, 3])
        self.assertRaises(TypeError, word2number, ['One', 'Two', 3])

