import Chem.Gases.IDLFunctions as IDLFunctions

variables = ('p', 'v', 'n', 't')

atmR = 0.08206
torrR = 62.36

while True:
    missing = input('Missing: ')
    if not missing in variables:
        print('Valid Values: p, v, n, t')
    else:
        break

given = IDLFunctions.given(missing)

if given.get('r') == 1:
    given.update({'r':atmR})
elif given.get('r') == 2:
    given.update({'r':torrR})
    
print(IDLFunctions.calculate(given, missing))