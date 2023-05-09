import MMFunctions
import SFunctions

while True:

    conversion = input('Conversion\n(ex: g mol): ')
    compound1 = input('1st Compound: ')
    amount = float(input(compound1 + ' amount \n(no units): '))
    compound2 = input('2nd Compound: ')
    coefficient1 = float(input(compound1 + ' Coeff: '))
    coefficient2 = float(input(compound2 + ' Coeff: '))
    
    conversion = conversion.split(' ')
   
    if not compound1 == compound2:
        MM1 = MMFunctions.calculate(compound1)
        MM2 = MMFunctions.calculate(compound2)
        same = False
    else:
        MM = MMFunctions.calculate(compound1)
        same = True

    if conversion[0] == 'g' and conversion[1] == 'g':
        mass = SFunctions.g_g(amount, MM1, coefficient1, coefficient2, MM2)
        print(str(round(mass, 3)) + 'g')
    elif conversion[0] == 'g' and conversion[1] == 'l':
        volume = SFunctions.g_l(amount, MM1, coefficient1, coefficient2)
        print(str(round(volume, 3)) + 'L')
    elif conversion[0] == 'g' and conversion[1] == 'mol':
        if not bool(same):
            mole = SFunctions.g_mol(amount, MM1, coefficient1, coefficient2)
            print(str(round(mole, 3)) + 'mol')
        elif bool(same):
            mole = SFunctions.mass_mole(amount, MM)
            print(str(round(mole, 3)) + 'mol')
    elif conversion[0] == 'mol' and conversion[1] == 'mol':
        mole = SFunctions.mole_mole(amount, coefficient1, coefficient2)
        print(str(round(mole, 3)) + 'mol')
    elif conversion[0] == 'mol' and conversion[1] == 'g':
        if not bool(same):
            mass = SFunctions.mol_g(amount, MM2, coefficient1, coefficient2)
            print(str(round(mass, 3)) + 'mol')
        elif bool(same):
            mass = SFunctions.mole_mass(amount, MM)
            print(str(round(mass, 3)) + 'mol')
    elif conversion[0] == 'mol' and conversion[1] == 'l':
        if not bool(same):
            volume = SFunctions.mol_l(amount, coefficient1, coefficient2)
            print(str(round(volume, 3)) + 'mol')
        elif compound1 == compound2:
            volume = SFunctions.mole_volume(amount)
            print(str(round(volume, 3)) + 'mol')
    elif conversion[0] == 'l' and conversion[1] == 'l':
        volume = SFunctions.l_l(amount, coefficient1, coefficient2)
        print(str(round(volume, 3)) + 'L')
    elif conversion[0] == 'l' and conversion[1] == 'g':
        mass = SFunctions.l_g(amount, MM2, coefficient1, coefficient2)
        print(str(round(mass, 3)) + 'g')
    elif conversion[0] == 'l' and conversion[1] == 'mol':
        if not bool(same):
            mole = SFunctions.l_mol(amount, coefficient1, coefficient2)
            print(str(round(mole, 3)) + 'mol')
        elif bool(same):
            mole = SFunctions.volume_mole(amount)
            print(str(round(mole, 3)) + 'mol')
        

    cont = input('Continue?: ')
    if cont.lower() == 'y':
        print(cont)
        continue
    else:
        break
