from random import randint
import json

dogs = []


class Dog:
    def __init__(self, id, age, height, weight) -> None:
        self.id = id
        self.name = Dog.fullname()
        self.age = age
        self.height = height
        self.weight = weight
        self.description = Dog.gen_description()

    @staticmethod
    def fullname():
        first_name = ["captain", "sailor", "tim", "bambee", "sally", "cutie"]
        last_name = ["bowsky", "moon", "ola", "bomboo", "somalee", "pipi"]
        return (
            first_name[randint(0, len(first_name) - 1)]
            + " "
            + last_name[randint(0, len(last_name) - 1)]
        )

    @staticmethod
    def gen_description():
        description_1 = ["healthy", "excited", "quiet", "active", "naughty", "jumpy"]
        description_2 = ["boy", "girl", "beast"]
        return (
            description_1[randint(0, len(description_1) - 1)]
            + " "
            + description_2[randint(0, len(description_2) - 1)]
        )

    def to_dict(self):
        return self.__dict__


for i in range(20):

    inst = Dog(i, randint(2, 11), randint(10, 80), randint(5, 30))

    dogs.append(inst.to_dict())


output = json.dumps({"dogs": dogs}, indent=4)

with open("data/dogs.json", "w") as file:
    file.write(output)
