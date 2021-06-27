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
        self.url = Dog.gen_url()

    @staticmethod
    def fullname():
        first_name = ["captain", "sailor", "tim", "bambee", "sally", "cutie"]
        last_name = ["bowsky", "moon", "ola", "bomboo", "somalee", "pipi"]
        return (
            first_name[randint(0, len(first_name) - 1)]
            + " "
            + last_name[randint(0, len(last_name) - 1)]
        ).title()

    @staticmethod
    def gen_description():
        description_1 = ["healthy", "excited", "quiet", "active", "naughty", "jumpy"]
        description_2 = ["boy", "girl", "beast"]
        return (
            description_1[randint(0, len(description_1) - 1)]
            + " "
            + description_2[randint(0, len(description_2) - 1)]
        ).title()

    @staticmethod
    def gen_url():
        url_list = [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjlZxhOG30OMIqLCT_sHdvirRXMmXi6Cu_qg&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZtmcKMAebCm9m1vdU5CJvbCUKMNLnaw3IRw&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlJeVu4Bd2mwTFx6j5Tsqr4e1i8VrS0ZFEPw&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCGV8IfpLKY1qZGRiF5V_BLulbmKk3uA9LyA&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNuoNuPRHT99qHNwA_kIwouhgqZgRhL_OX-w&usqp=CAU",
        ]
        return url_list[randint(0, len(url_list) - 1)]

    def to_dict(self):
        return self.__dict__


for i in range(20):

    inst = Dog(i, randint(2, 11), randint(10, 80), randint(5, 30))

    dogs.append(inst.to_dict())


output = json.dumps({"dogs": dogs}, indent=4)

with open("data/dogs.json", "w") as file:
    file.write(output)
