from .utils import get_random_index

class Box(object):
    def __init__(self):
        self.practice = []
        self.to_review = []
        self.known = []

    def add_card(self, card):
        self.practice.append(card)

    def get_card(self):
        if self.practice:
            index = get_random_index(self.to_practice)
            return self.to_practice.pop(index), "practice"
