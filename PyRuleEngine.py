'''Library to implement hashcat style rule engine.'''
import re
#based on hashcat rules from
#https://hashcat.net/wiki/doku.php?id=rule_based_attack

def i36(string):
    '''Shorter way of converting base 36 string to integer'''
    return int(string, 36)
__rules__ = [
    ':', 'l', 'u', 'c', 'C', 't', r'T\w', 'r', 'd', r'p\w', 'f', '{',
    '}', '$.', '^.', '[', ']', r'D\w', r'x\w\w', r'O\w\w', r'i\w.',
    r'o\w.', r'\'\w', 's..', '@.', r'z\w', r'Z\w', 'q',
    ]

for i, func in enumerate(__rules__):
    __rules__[i] = func[0]+func[1:].replace(r'\w', '[a-zA-Z0-9]')
__ruleregex__ = '|'.join(['%s%s' % (re.escape(a[0]), a[1:]) for a in __rules__])
__ruleregex__ = re.compile(__ruleregex__)


FUNCTS = {}
FUNCTS[':'] = lambda x, i: x
FUNCTS['l'] = lambda x, i: x.lower()
FUNCTS['u'] = lambda x, i: x.upper()
FUNCTS['c'] = lambda x, i: x.capitalize()
FUNCTS['C'] = lambda x, i: x.capitalize().swapcase()
FUNCTS['t'] = lambda x, i: x.swapcase()
FUNCTS['T'] = lambda x, i: x[0:i36(i[1])]+x[i36(i[1])].swapcase()+x[i36(i[1])+1:]
FUNCTS['r'] = lambda x, i: x[::-1]
FUNCTS['d'] = lambda x, i: x+x
FUNCTS['p'] = lambda x, i: x*(i36(i[1])+1)
def interpret_rule(word, rule):
    '''Apply rule to given word'''
    for function in __ruleregex__.findall(rule):
        try:
            word = FUNCTS[function[0]](word, function)
        except KeyError:
            print('Unknown rule:', function)
        except IndexError:
            pass
    return word
