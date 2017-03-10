import unittest
from PyRuleEngine import InterpretRule as IR
class RuleTest(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(IR('p@ssW0rd', ':'), 'p@ssW0rd')
    def test_lowercase(self):
        self.assertEqual(IR('p@ssW0rd', 'l'), 'p@ssw0rd')
    def test_uppercase(self):
        self.assertEqual(IR('p@ssW0rd', 'u'), 'P@SSW0RD')
    def test_capitalize(self):
        self.assertEqual(IR('p@ssW0rd', 'c'), 'P@ssw0rd')
    def test_inverted_capitalize(self):
        self.assertEqual(IR('p@ssW0rd', 'C'), 'p@SSW0RD')
    def test_toggle_case(self):
        self.assertEqual(IR('p@ssW0rd', 't'), 'P@SSw0RD')
    def test_toggle_N(self):
        self.assertEqual(IR('p@ssW0rd', 'T3'), 'p@sSW0rd')
    def test_reverse(self):
        self.assertEqual(IR('p@ssW0rd', 'r'), 'dr0Wss@p')
    def test_duplicate(self):
        self.assertEqual(IR('p@ssW0rd', 'd'), 'p@ssW0rdp@ssW0rd')
    def test_duplicate_N(self):
        self.assertEqual(IR('p@ssW0rd', 'p2'), 'p@ssW0rdp@ssW0rdp@ssW0rd')

if __name__ == '__main__':
    unittest.main()
