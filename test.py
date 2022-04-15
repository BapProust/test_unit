from Module import *


def test_person_init():
    person = Person("Mahmoud")

    assert person.name == "Mahmoud"
    assert person.life_points == 100


def test_person_hit():
    person = Person("Mahmoud")

    assert person.get_life_points() == 100


def test_person_is_dead():
    person = Person("Mahmoud")

    assert person.is_dead() == False

    person.life_points = 0

    assert person.is_dead() == True


def test_person_gained_life_points():
    person = Person("Mahmoud")
    person.hit(person)
    person.gained_life_points(10)

    assert person.get_life_points() == 100


def test_person_get_life_points():
    person = Person("Mahmoud")

    assert person.get_life_points() == 100


def test_wizard_init():
    wizzard = Wizard("Airbus Dumbledore 280")

    assert wizzard.name == "Airbus Dumbledore 280"
    assert wizzard.get_life_points() == 80


def test_wizard_hit():
    wizzard = Wizard("Airbus Dumbledore 280")
    wizzard.hit(wizzard)
    assert wizzard.get_life_points() == 65


def test_healthpotion_was_used_by():
    person = Person("Mahmoud")
    HealthPotion.was_used_by(person)

    assert person.get_life_points() == 110
