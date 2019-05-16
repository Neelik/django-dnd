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


def orm_ify_query_params(query_params, model: str):
    """
    Method to convert user friendly query parameters to Django-ORM accepted filter keywords

    :param query_params: Dictionary of query parameters passed to the API
    :param model: String representing the name of a model, e.g. "Character"
    :return: Dictionary that can be directly unpacked into Django's .filter()
    """

    # Lookup table to convert the API query terms to Django ORM keywords, by model
    model_field_lookup = {
        "Ability Score": {
            "intelligence": "intelligence",
            "intelligence_above": "intelligence__gte",
            "intelligence_below": "intelligence__lte",
            "strength": "strength",
            "strength_above": "strength__gte",
            "strength_below": "strength__lte",
            "dexterity": "dexterity",
            "dexterity_above": "dexterity__gte",
            "dexterity_below": "dexterity__lte",
            "constitution": "constitution",
            "constitution_above": "constitution__gte",
            "constitution_below": "constitution__lte",
            "wisdom": "wisdom",
            "wisdom_above": "wisdom__gte",
            "wisdom_below": "wisdom__lte",
            "charisma": "charisma",
            "charisma_above": "charisma__gte",
            "charisma_below": "charisma__lte",
        }
    }

    fields = model_field_lookup[model]
    query_dict = {}

    for key, value in query_params.items():
        query_dict.update({fields[key]: value})

    return query_dict
