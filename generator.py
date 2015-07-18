import random


class Generator:
    def __init__(self):
        self.testimonies = []

    def add_testimony(self, new_testimony):
        self.testimonies.append(new_testimony)

    def remove_testimony(self, testimony):
        self.testimonies.remove(testimony)

    def generate_testimony(self):
        random_index = int(random.random()) % len(self.testimonies)

        return self.testimonies[random_index]

    def has_testimony(self, testimony):
        return testimony in self.testimonies

    def __str__(self):
        pass
