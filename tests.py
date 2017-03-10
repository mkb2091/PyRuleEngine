import unittest
from PyRuleEngine import InterpretRule as IR
class RuleTest(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(IR('p@ssW0rd', ':'), 'p@ssW0rd')
    def test_lowercase(self):
        self.assertEqual(IR('p@ssW0rd', 'l'), 'p@ssw0rd')
    def test_lowercase(self):
        self.assertEqual(IR('p@ssW0rd', 'u'), 'P@SSW0RD')

if __name__ == '__main__':
    unittest.main()
