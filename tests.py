import unittest
from PyRuleEngine import RuleEngine
RULEENGINE = RuleEngine([])


def IR(word, rule):
    RULEENGINE.change_rules([rule])
    return list(RULEENGINE.apply(word))[0]


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

    def test_toggle_n(self):
        self.assertEqual(IR('p@ssW0rd', 'T3'), 'p@sSW0rd')

    def test_reverse(self):
        self.assertEqual(IR('p@ssW0rd', 'r'), 'dr0Wss@p')

    def test_duplicate(self):
        self.assertEqual(IR('p@ssW0rd', 'd'), 'p@ssW0rdp@ssW0rd')

    def test_duplicate_n(self):
        self.assertEqual(IR('p@ssW0rd', 'p2'), 'p@ssW0rdp@ssW0rdp@ssW0rd')

    def test_reflect(self):
        self.assertEqual(IR('p@ssW0rd', 'f'), 'p@ssW0rddr0Wss@p')

    def test_rotate_left(self):
        self.assertEqual(IR('p@ssW0rd', '{'), '@ssW0rdp')

    def test_rotate_right(self):
        self.assertEqual(IR('p@ssW0rd', '}'), 'dp@ssW0r')

    def test_append(self):
        self.assertEqual(IR('p@ssW0rd', '$1'), 'p@ssW0rd1')

    def test_prepend(self):
        self.assertEqual(IR('p@ssW0rd', '^1'), '1p@ssW0rd')

    def test_truncate_left(self):
        self.assertEqual(IR('p@ssW0rd', '['), '@ssW0rd')

    def test_truncate_right(self):
        self.assertEqual(IR('p@ssW0rd', ']'), 'p@ssW0r')

    def test_delete_n(self):
        self.assertEqual(IR('p@ssW0rd', 'D3'), 'p@sW0rd')

    def test_extract_range(self):
        self.assertEqual(IR('p@ssW0rd', 'x04'), 'p@ss')

    def test_omit_range(self):
        self.assertEqual(IR('p@ssW0rd', 'O12'), 'psW0rd')

    def test_insert(self):
        self.assertEqual(IR('p@ssW0rd', 'i4!'), 'p@ss!W0rd')

    def test_overwrite(self):
        self.assertEqual(IR('p@ssW0rd', 'o3$'), 'p@s$W0rd')

    def test_truncate_n(self):
        self.assertEqual(IR('p@ssW0rd', "'6"), 'p@ssW0')

    def test_replace(self):
        self.assertEqual(IR('p@ssW0rd', 'ss$'), 'p@$$W0rd')

    def test_purge(self):
        self.assertEqual(IR('p@ssW0rd', '@s'), 'p@W0rd')

    def test_duplicate_first_n(self):
        self.assertEqual(IR('p@ssW0rd', 'z2'), 'ppp@ssW0rd')

    def test_duplicate_last_n(self):
        self.assertEqual(IR('p@ssW0rd', 'Z2'), 'p@ssW0rddd')

    def test_duplicate_all(self):
        self.assertEqual(IR('p@ssW0rd', 'q'), 'pp@@ssssWW00rrdd')
if __name__ == '__main__':
    unittest.main()
