from django.db import models


class EditMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def get_ability_score_increase(race):
    increases_by_race = {
        "hill dwarf": {
            "Constitution": 2,
            "Wisdom": 1
        },
        "mountain dwarf": {
            "Constitution": 2,
            "Strength": 2
        },
        "high elf": {
            "Dexterity": 2,
            "Intelligence": 1
        },
        "dark elf": {
            "Dexterity": 2,
            "Charisma": 1
        },
        "wood elf": {
            "Dexterity": 2,
            "Wisdom": 1
        },
        "lightfoot halfling": {
            "Dexterity": 2,
            "Charisma": 1
        },
        "stout halfling": {
            "Dexterity": 2,
            "Constitution": 1
        },
        "human": {
            "Strength": 1,
            "Constitution": 1,
            "Dexterity": 1,
            "Intelligence": 1,
            "Wisdom": 1,
            "Charisma": 1
        },
        "dragonborn": {
            "Strength": 2,
            "Charisma": 1
        },
        "forest gnome": {
            "Intelligence": 2,
            "Dexterity": 1
        },
        "rock gnome": {
            "Intelligence": 2,
            "Constitution": 1
        },
        "half-elf": {
            "Charisma": 2,
            "Strength": 1,
            "Dexterity": 1,
            "Constitution": 1,
            "Intelligence": 1,
            "Wisdom": 1
        },
        "half-orc": {
            "Strength": 2,
            "Constitution": 1
        },
        "tiefling": {
            "Intelligence": 1,
            "Charisma": 2
        }
    }

    return increases_by_race[race]
