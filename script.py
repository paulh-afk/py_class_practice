class Dog:
    def __init__(self, input_name, input_breed, input_age=0, input_friendliness=True):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = input_friendliness

    def have_birthday(self):
        self.age += 1
        print(self.name, 'is now', self.age, 'yo!')


dog_one = Dog('Medor', 'Golden Retriever', 9, True)

dog_one.have_birthday()
