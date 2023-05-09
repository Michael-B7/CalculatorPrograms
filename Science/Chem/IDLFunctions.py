def given(missing):
    given = {}
    if not missing == 'p':
        p = float(input('P: '))
        given.update({'p':p})
    r = float(input('atm (1) / torr (2): '))
    given.update({'r':r})
    if not missing == 'v':
        v = float(input('V: '))
        given.update({'v':v})
    if not missing == 'n':
        n = float(input('n: '))
        given.update({'n':n})
    if not missing == 't':
        t = float(input('T: '))
        given.update({'t':t})
    return given

def calculate(given, missing):
    if missing == 'p':
        if given.get('r') == 0.08206:
            units = 'atm'
        else:
            units = 'torr'
        bottom = given.get('v')
        top = given.get('n') * given.get('r') * given.get('t')
        answer = str(top / bottom) + ' ' + units
    elif missing == 'v':
        units = 'L'
        bottom = given.get('p')
        top = given.get('n') * given.get('r') * given.get('t')
        answer = str(top / bottom) + units
    elif missing == 'n':
        units = 'mol'
        top = given.get('p') * given.get('v')
        bottom = given.get('r') * given.get('t')
        answer = str(top / bottom) + ' ' + units
    elif missing == 't':
        units = 'K'
        top = given.get('p') * given.get('v')
        bottom = given.get('r') * given.get('n')
        answer = str(top / bottom) + units
    return answer