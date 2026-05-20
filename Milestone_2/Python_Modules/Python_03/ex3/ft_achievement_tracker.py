#!/usr/bin/env python3


import random


ACHIEVEMENT_LIST = [
    "First Blood",
    "Hoarder",
    "Unstoppable",
    "MacGyver",
    "Glutton for Punishment",
    "Pacifist",
    "Speed Runner",
    "Cartographer",
    "Myth Buster",
    "Team Player",
    "Overkill",
    "Sneak Thief",
    "Loremaster",
    "Fashion Victim",
    "Breaking the Matrix",
    "Eco-Friendly",
    "Penny Pincher",
    "Animal Lover",
    "Insomniac",
    "Serious Dedication"
]


def gen_player_achievements() -> set:
    num_elements: int = random.randint(0, len(ACHIEVEMENT_LIST))
    rand_set: set = set(random.sample(ACHIEVEMENT_LIST, k=num_elements))

    return rand_set


if __name__ == "__main__":
    Alice: set = gen_player_achievements()
    Bob: set = gen_player_achievements()
    Charlie: set = gen_player_achievements()
    Dylan: set = gen_player_achievements()
