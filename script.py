class Dog:
    def __init__(self, input_name, input_breed, input_age=0, input_friendliness=True):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = input_friendliness
        self.friends = []

    def have_birthday(self):
        self.age += 1
        print(self.name, 'is now', self.age, 'yo!')

    def add_friend(self, dog):
        if dog.is_friendly:
            self.friends.append(dog)

    def friends_list(self):
        for dog in self.friends:
            print(dog.name, 'is a friend of', self.name,
                  'and he is', self.age, 'yo')


dog_one = Dog('Medor', 'Golden Retriever', 9, True)
dog_two = Dog('Huck', 'Akita', 2, True)
dog_three = Dog('Tik', 'Australian Shepherd', 2, True)

dog_one.add_friend(dog_two)
dog_one.add_friend(dog_three)

dog_one.friends_list()
