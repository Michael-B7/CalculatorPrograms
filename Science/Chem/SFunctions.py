def mass_mole (g, MM):
    mole = g / MM
    return mole

def mole_mole (mol, co1, co2):
    ratio = co2 / co1
    mole = mol * ratio
    return mole

def mole_mass(mol,MM):
    mass = mol * MM
    return mass

def volume_mole(amount):
    mole = amount / 22.4
    return mole

def mole_volume(mol):
    volume = mol * 22.4
    return volume

def g_g(amount, MM1, co1, co2, MM2):
    mole1 = mass_mole(amount, MM1)
    mole2 = mole_mole(mole1, co1, co2)
    mass = mole_mass(mole2, MM2)
    return mass

def g_l(amount, MM, co1, co2):
    mole1 = mass_mole(amount, MM)
    mole2 = mole_mole(mole1, co1, co2)
    volume = mole_volume(mole2)
    return volume

def g_mol(amount, MM, co1, co2):
    mole1 = mass_mole(amount, MM)
    mole2 = mole_mole(mole1, co1, co2)
    return mole2

def mol_g(amount, MM, co1, co2):
    mole = mole_mole(amount, co1, co2)
    mass = mole_mass(mole, MM)
    return mass

def mol_l(amount, co1, co2):
    mole = mole_mole(amount, co1, co2)
    volume = mole_volume(mole)
    return volume

def l_l(amount, co1, co2):
    mole1 = volume_mole(amount)
    mole2 = mole_mole(mole1, co1, co2)
    volume = mole_volume(mole2)
    return volume

def l_g(amount, MM, co1, co2):
    mole1 = volume_mole(amount)
    mole2 = mole_mole(mole1, co1, co2)
    mass = mole_mass(mole2, MM)
    return mass

def l_mol(amount, co1, co2):
    mole1 = volume_mole(amount)
    mole2 = mole_mole(mole1, co1, co2)

