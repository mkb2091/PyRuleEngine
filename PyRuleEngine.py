import re
#based on hashcat rules from
#https://hashcat.net/wiki/doku.php?id=rule_based_attack
i36=lambda x: int(x, 36)
__rules__=[
    ':', 'l', 'u', 'c', 'C', 't', 'T\w', 'r', 'd', 'p\w', 'f', '{',
    '}', '$.', '^.', '[', ']', 'D\w', 'x\w\w', 'O\w\w', 'i\w.',
    'o\w.', '\'\w', 's..', '@.', 'z\w', 'Z\w', 'q',
    ]

for i in range(len(__rules__)):
    __rules__[i]=__rules__[i][0]+__rules__[i][1:].replace('\w', '[a-zA-Z0-9]')
__ruleregex__='|'.join(['%s%s' % (re.escape(a[0]), a[1:]) for a in __rules__])
__ruleregex__=re.compile(__ruleregex__)

functs={}
functs[':'] = lambda x, i: x
functs['l'] = lambda x, i: x.lower()
functs['u'] = lambda x, i: x.upper()
functs['c'] = lambda x, i: x.capitalize()
functs['C'] = lambda x, i: x.capitalize().swapcase()
functs['t'] = lambda x, i: x.swapcase()
functs['T'] = lambda x, i: x[0:i36(i[1])]+x[i36(i[1])].swapcase()+x[i36(i[1])+1:]
functs['r'] = lambda x, i: x[::-1]
functs['d'] = lambda x, i: x+x
functs['p'] = lambda x, i: x*(i36(i[1])+1)
def InterpretRule(word, rule):
    for r in __ruleregex__.findall(rule):
        try:
            word=functs[r[0]](word, r)
        except KeyError:
            print('Unknown rule:', rule)
        except Exception as error:
            print(type(error),error)
    return word
