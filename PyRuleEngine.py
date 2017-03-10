import re
#based on hashcat rules from
#https://hashcat.net/wiki/doku.php?id=rule_based_attack
b_int=int
int=lambda x: b_int(x, 36)
__rules__=[
    ':', 'l', 'u', 'c', 'C', 't', 'T\w', 'r', 'd', 'p\w', 'f', '{',
    '}', '$.', '^.', '[', ']', 'D\w', 'x\w\w', 'O\w\w', 'i\w.',
    'o\w.', '\'\w', 's..', '@.', 'z\w', 'Z\w', 'q',
    ]

for i in range(len(__rules__)):
    __rules__[i]=__rules__[i][0]+__rules__[i][1:].replace('\w', '[a-zA-Z0-9]')
__ruleregex__='|'.join(['%s%s' % (re.escape(a[0]), a[1:]) for a in __rules__])
__ruleregex__=re.compile(__ruleregex__)

functions={}
functions[':']=lambda x, i: x
functions['l']=lambda x, i: x.lower()
functions['u']=lambda x, i: x.upper()
functions['c']=lambda x, i: x.capitalize()
def InterpretRule(word, rule):
    for r in __ruleregex__.findall(rule):
        try:
            word=functions[r[0]](word, r)
        except Exception as error:
            print(error)
    return word
