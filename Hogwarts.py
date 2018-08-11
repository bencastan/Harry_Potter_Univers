class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881, 'male')


class Pupil(HogwartsMember):
    """
    Create a Hogwarts Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._owls = {
            'Study of Ancient Runes': False,
            'Arithmancy': False,
            'Astronomy': False,
            'Care of Magical Creature': False,
            'Defence Against the Dark Arts': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Muggle Studies': False,
            'Potions': False,
            'Transformations': False
        }

    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Griffindor', 1991, ('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronald Bilius Weasley', 1980, 'male', 'Griffindor', 1991, ('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        return cls('Hermione', 1979, 'female', 'Griffindor', 1991, ('Crookshanks', 'cat'))


class Professor(HogwartsMember):
    """
    Creates a Hogwarts Professor
    """

    def __init__(self, name, birthyear, sex, subject, house=None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', 'Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', 'Slytherin')

class Ghost(HogwartsMember):
    """
    Creates a Hogwarts Ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house


if __name__ == "__main__":

    hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1928,sex='male')
    harry = Pupil(name='Harry James Potter', birthyear=1980, house='Griffindor', start_year=1991, sex='male')
    headmaster = harry.school_headmaster()

    mcgonagall = Professor.mcgonagall()
    snape = Professor.snape()
    harry = Pupil.harry()
    ron = Pupil.ron()
    hermione = Pupil.hermione()
