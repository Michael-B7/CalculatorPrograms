class Equation(object):
    def __init__(self):
        self.given = input("Given: ")
        self.givenValue = float(input("Given Value: "))
        self.calculate(self.given)
        
    def calculate(self, given):
        if(given.lower() == "e"):
            equation = 'Frequency: ' + "{:.3e}".format(self.givenValue / h)
        elif(given.lower() == "w"):
            equation = 'Frequency: ' + "{:.3e}".format(c / self.givenValue)
        else:
            missing = input("Missing: ")
            if(missing.lower() == "e"):
                equation = 'Energy: ' + "{:.3e}".format(h * self.givenValue)
            else:
                equation = 'Wavelength: ' + "{:.3e}".format(c / self.givenValue)
        self.result = equation

c = 2.998e+8
h = 6.626e-34

equation = Equation()
print(equation.result)