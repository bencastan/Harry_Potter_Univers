import datetime


class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881, 'male')

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Pupil(HogwartsMember):
    """
    Create a Hogwarts Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple=None):
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

    @property
    def owls(self):
        return self._owls

    @owls.setter
    def owls(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass an interable with two items: subject and grade")

        passwd = self.passed(grade)

        if passed:
            self.owls[subject] = True
        else:
            print("The exam was not passed so no OWL was awarded!")

    @owls.deleter
    def owls(self):
        print("caution, you are deleting this students' OWL's! "
              "you should only do that if she / he dropped out of school without passing any exam!")
        del self._owls


    @staticmethod
    def passed(grade):
        """
        Give a grade, determine if an exam was passed
        :param grade:
        :return:
        """
        grades = {
            'O': True,
            'Ordinary': True,
            'P' : True,
            'Passed': True,
            'A': True,
            'Acceptable': True,
            'P': False,
            'Poor': False,
            'D': False,
            'Dreadful': False,
            'T': False,
            'Troll': False,
        }

        return grades.get(grade, False)

    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Griffindor', 1991, ('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronald Bilius Weasley', 1980, 'male', 'Griffindor', 1991, ('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        return cls('Hermione', 1979, 'female', 'Griffindor', 1991, ('Crookshanks', 'cat'))

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")


class Professor(HogwartsMember):
    """
    Creates a Hogwarts Professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house=None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', 'Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', 'Slytherin')

    @property
    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts Ghost
    """

    def __init__(self, name:str, birthyear: int, sex: str, year_of_death: int, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")


if __name__ == "__main__":

    hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1928,sex='male')
    print(hagrid.age)
    harry = Pupil(name='Harry James Potter', birthyear=1980, house='Griffindor', start_year=1991, sex='male')
    headmaster = harry.school_headmaster()

    mcgonagall = Professor.mcgonagall()
    snape = Professor.snape()
    harry = Pupil.harry()
    ron = Pupil.ron()
    hermione = Pupil.hermione()
