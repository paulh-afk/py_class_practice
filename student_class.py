class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        return '{name}, year {year}'.format(name=self.name, year=self.year)


roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

print(roger)
print(sandro)
print(pieter)
