# coding=utf-8
from __future__ import unicode_literals
from ..es_ES import Provider as PersonProvider


class Provider(PersonProvider):
    """
    Adds popular Catalan names.
    https://www.idescat.cat/pub/?id=aec&n=946&lang=es&t=2018
    https://www.idescat.cat/pub/?id=aec&n=947&lang=es&t=2018
    """
    first_names_male = (
        'Adam',
        'Albert',
        'Aleix',
        'Álex',
        'Antonio',
        'Arnau',
        'Biel',
        'Bruno',
        'Carlos',
        'Daniel',
        'David',
        'Enzo',
        'Èric',
        'Francisco',
        'Hugo',
        'Jan',
        'Javier',
        'Joan',
        'Jordi',
        'Jorge',
        'Josep',
        'José',
        'José María',
        'Juan',
        'Leo',
        'Lucas',
        'Manuel',
        'Marc',
        'Martí',
        'Max',
        'Miguel',
        'Nil',
        'Pau',
        'Pedro',
        'Pol',
        'Ramón',
        'Xavier')

    first_names_female = (
        'Abril',
        'Aina',
        'Ana',
        'Anna',
        'Antonia',
        'Antònia',
        'Arlet',
        'Carla',
        'Carmen',
        'Chlóe',
        'Clàudia',
        'Cristina',
        'Dolores',
        'Emma',
        'Francisca',
        'Isabel',
        'Jana',
        'Josefa',
        'Júlia',
        'Laia',
        'Laura',
        'Lucia',
        'Marta',
        'Martina',
        'María',
        'María Del Carmen',
        'María Dolores',
        'María Teresa',
        'Mia',
        'Montserrat',
        'Noa',
        'Núria',
        'Ona',
        'Paula',
        'Rosa',
        'Sara',
        'Sofía',
        'Sílvia',
        'Valèria')

    first_names = first_names_male + first_names_female
