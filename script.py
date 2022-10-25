class Dog:
    def __init__(self, input_name, input_breed, input_age=0, input_friendliness=True):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = input_friendliness
        self.friends = []

    def __repr__(self):
        description = 'This {breed} named {name} is {age} years old and has {number_of_friends} friends. '.format(
            breed=self.breed, name=self.name, age=self.age, number_of_friends=len(self.friends))

        if self.is_friendly:
            description += '{} is a friendly dog.'.format(self.name)
        else:
            description += '{} is an unfriendly dog.'.format(self.name)

        return description

    def have_birthday(self):
        self.age += 1
        print(self.name, 'is now', self.age, 'yo!')

    def become_friends(self, other_dog):
        if other_dog.is_friendly:
            self.friends.append(other_dog)
            other_dog.friends.append(self)

            print('{name} is a friend of {other_name} who is {other_age} yo!'.format(
                name=self.name, other_name=other_dog.name, other_age=other_dog.age))

        else:
            print("{other_name} did not want to become friends with {name}!".format(
                name=self.name, other_name=other_dog.name))


dog_one = Dog('Medor', 'Golden Retriever', 9, True)
dog_two = Dog('Huck', 'Akita', 2, True)
dog_three = Dog('Tik', 'Australian Shepherd', 2, False)

dog_one.become_friends(dog_two)
dog_one.become_friends(dog_three)

print(dog_one)
print(dog_two)
print(dog_three)
