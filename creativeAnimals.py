import json
import random


def get_adjective():
    f = open('adjectives.json')
    data = json.load(f)  # returns JSON object as a dictionary
    # print(len(data))
    # for i in data:
    #     print(i)
    f.close()
    random.shuffle(data)
    return data[0]


def get_animal(adjective):
    f = open('animals.json')
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()
    letter = adjective[:1].lower()
    matchedAnimals = data[letter]
    random.shuffle(matchedAnimals)
    return matchedAnimals[0]

    # print(len(data))
    # for i in data:
    #     print(i)


def run():
    adjective = get_adjective()
    animal = get_animal(adjective)
    out = adjective + " " + animal + " "
    print(out)


# x = get_adjective()
# print(x)

# y = get_animal(x)
# print(y)

# run()

for x in range(151):
  run()