import Chem.MolarMass.MMFunctions as MMFunctions

while True:
    chemical = input('Compound: ')
    print(str(MMFunctions.calculate(chemical)) + ' g/mol')

    cont = input('Continue?: ')

    if cont.lower() == 'y':
        continue
    else:
        break