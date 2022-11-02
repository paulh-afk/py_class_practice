class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def __repr__(self):
        return '{name}, year {year}'.format(name=self.name, year=self.year)

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

    def get_average(self):
        try:
            total = 0
            for grade in self.grades:
                total += grade.score

            return total / len(self.grades)
        except ZeroDivisionError:
            return 0


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= self.minimum_passing


roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

pieter_grade_1 = Grade(100)
pieter_grade_2 = Grade(50)

pieter.add_grade(pieter_grade_1)
pieter.add_grade(pieter_grade_2)

print(pieter.get_average())
print(sandro.get_average())

print(pieter_grade_1.is_passing())
print(pieter_grade_2.is_passing())
