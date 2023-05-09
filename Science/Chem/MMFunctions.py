MASSES = {
    'H': 1.01, 'He': 4.00, 'Li': 6.94, 'Be': 9.01, 'B': 10.81, 'C': 12.01, 'N': 14.01, 'O': 16.00, 
    'F': 19.00, 'Ne': 20.18, 'Na': 22.99, 'Mg': 24.31, 'Al': 26.98, 'Si': 28.09, 'P': 30.97, 'S': 32.07,
    'Cl': 35.45, 'Ar': 39.95, 'K': 39.10, 'Ca': 40.08, 'Sc': 44.96, 'Ti': 47.87, 'V': 50.94, 'Cr': 2.00, 
    'Mn': 54.94, 'Fe': 55.85, 'Co': 58.93, 'Ni': 58.69, 'Cu': 63.55, 'Zn': 65.39, 'Ga': 69.72, 'Ge': 72.61,
    'As': 74.92, 'Se': 78.96, 'Br': 79.90, 'Kr': 83.80, 'Rb': 85.47, 'Sr': 87.62, 'Y': 88.91, 'Zr': 91.22,
    'Nb': 92.91, 'Mo': 95.94, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87, 
    'Cd': 112.41, 'In': 114.82, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.60, 'I': 126.90, 'Xe': 131.29, 
    'Cs': 132.91, 'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24, 'Pm': 145, 
    'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93, 'Dy': 162.50, 'Ho': 164.93, 'Er': 167.26, 
    'Tm': 168.93, 'Yb': 173.04, 'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21, 
    'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59, 'Tl': 204.38, 'Pb': 207.2, 
    'Bi': 208.98, 'Po': 209, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232.04, 
    'Pa': 231.04, 'U': 238.03, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247, 'Cf': 251, 
    'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 261, 'Db': 262, 'Sg': 266, 'Bh': 264, 
    'Hs': 269, 'Mt': 268, 'Ds': 281, 'Rg': 280, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 288, 'Lv': 293, 
    'Ts': 294, 'Og': 294}
    
def find_parenthesis(compound):
    global parenthesis
    global parenthesis_list
    parenthesis_list = []
    parenthesis = ''
    for i in range(0,len(compound)):
        if compound[i:i+1] == '(':
            for x in range(i,len(compound)):
                if compound[x:x+1] == ')' and compound[x+1:x+2].isdigit() and not compound[x+2:x+3].isdigit():
                    a = compound[i+1:x+2]
                    parenthesis = compound[i:x+2]
                    parenthesis_list = a.split(')')
                elif compound[x:x+1] == ')' and compound[x+1:x+2].isdigit() and compound[x+2:x+3].isdigit():
                    a = compound[i+1:x+3]
                    parenthesis = compound[i:x+3]
                    parenthesis_list = a.split(')')

def find_numbers(compound):
    global numbers
    numbers = []
    for i in range(0,len(compound)):
        if compound[i:i+1].isdigit() and not compound[i+1:i+2].isdigit() and not compound[i-1:i].isdigit():
            numbers.append(compound[i:i+1])
        elif compound[i:i+1].isdigit() and compound[i+1:i+2].isdigit():
            numbers.append(compound[i:i+2])
        elif not compound[i:i+1].isdigit() and compound[i+1:i+2].isupper():
            numbers.append(1)
        elif not compound[i:i+1].isdigit() and compound[i+1:i+2] == '':
            numbers.append(1)

def separate(compound):
    global chemicals
    chemicals = []
    x = compound
    for i in range(0,len(numbers)):
        if isinstance(numbers[i], str):
            x = x.replace(numbers[i], ' ', 1)
    x = x.split(' ')
    if x[-1] == '':
        for i in range(0, len(x)-1):
            if x[i] in MASSES:   
                chemicals.append(x[i])
            elif x[i] not in MASSES:
                for a in range(0,len(x[i])):
                    b = str(x[i])
                    if b[a:a+1].islower():
                        chemicals.append(b[a-1:a+1])
                    elif b[a:a+1].isupper() and b[a+1:a+2].isupper() or b[a:a+1].isupper() and b[a+1:a+2] == '':
                        chemicals.append(b[a:a+1])
    else:
        for i in range(0, len(x)):
            if x[i] in MASSES:   
                chemicals.append(x[i])
            elif x[i] not in MASSES:
                for a in range(0,len(x[i])):
                    b = str(x[i])
                    if b[a:a+1].islower():
                        chemicals.append(b[a-1:a+1])
                    elif b[a:a+1].isupper() and b[a+1:a+2].isupper() or b[a:a+1].isupper() and b[a+1:a+2] == '':
                        chemicals.append(b[a:a+1])
    
def calculate(compound):
    find_parenthesis(compound)
    chem = compound.replace(parenthesis, '')
    global molar_mass
    molar_mass = 0
    if bool(parenthesis_list):
        find_numbers(parenthesis_list[0])
        numbers.append(parenthesis_list[1])
        separate(parenthesis_list[0])
        new_numbers = []
        for i in range(0,len(numbers)-1):
            new_numbers.append(int(numbers[-1]) * int(numbers[i]))
        for i in range(0,len(chemicals)):
            molar_mass = molar_mass + (MASSES[chemicals[i]] * int(new_numbers[i]))
    if not parenthesis == compound:
        find_numbers(chem)
        separate(chem)
        for i in range(0,len(chemicals)):
            molar_mass = molar_mass + (MASSES[chemicals[i]]) * int(numbers[i])
    return round(molar_mass, 2)
