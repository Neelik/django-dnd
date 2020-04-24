from django.db import models
from rest_framework import status
from rest_framework.response import Response

import copy

RESPONSES = {
    '200': {},
    '201': {},
    '400': {
        'message': 'One or more required fields are missing.',
        'userMessage': 'We were unable to process your request due to an error. Please check all fields and try again.',
        'errors': []
    },
    '401': {
        'message': 'Unauthorized request',
        'userMessage': 'Sorry, you are not authorized to perform this action.',
        'errors': []
    },
    '403': {
        'message': 'Forbidden to perform action',
        'userMessage': 'You are not allowed to perform the requested action.',
        'errors': []
    },
    '404': {
        'message': 'Resource does not exist.',
        'userMessage': 'The resource you requested was not found.',
        'errors': []
    },
    '409': {
        'message': 'Resource already exists.',
        'userMessage': 'We were unable to save your data since it already exists.',
        'errors': []
    },
    '500': {
        'message': 'Internal server error',
        'userMessage': 'The server was unable to process your request due to an internal error. Please try again.',
        'errors': []
    },
    '501': {
        'message': 'Feature not yet implemented.',
        'userMessage': 'Your request is not allowed at the moment.',
        'errors': []
    }
}

# See https://github.com/RonquilloAeon/Monky-Trends-API-Guidelines
STATUS_CODES = {
    '200': status.HTTP_200_OK,
    '201': status.HTTP_201_CREATED,
    '400': status.HTTP_400_BAD_REQUEST,
    '401': status.HTTP_401_UNAUTHORIZED,
    '403': status.HTTP_403_FORBIDDEN,
    '404': status.HTTP_404_NOT_FOUND,
    '409': status.HTTP_409_CONFLICT,
    '500': status.HTTP_500_INTERNAL_SERVER_ERROR,
    '501': status.HTTP_501_NOT_IMPLEMENTED
}


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
        "Character": {
            "name": "name__icontains",
            "player": "player_name__icontains",
            "class": "character_class__iexact",
            "race": "race__iexact",
            "level_above": "level__gte",
            "level_below": "level__lte"
        },
        "NPC": {
            "name": "name__icontains",
            "class": "npc_class__iexact",
            "race": "race__iexact",
            "level_above": "level__gte",
            "level_below": "level__lte"
        },
        "Equipment": {
            "id": "id__iexact",
            "equipment_name": "equipment_name__icontains",
            "equipment_type": "equipment_type__iexact",
            "is_magic": "is_magic"
        },
        "Background": {
            "name": "name__icontains",
            "spec": "spec__icontains",
            "equipment": "equipment__icontains"
        },
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
        },
        "Skills": {
            "acrobatics": "acrobatics",
            "acrobatics_above": "acrobatics__gte",
            "acrobatics_below": "acrobatics__lte",
            "animal_handling": "animal_handling",
            "animal_handling_above": "animal_handling_gte",
            "animal_handling_below": "animal_handling_lte",
            "arcana": "arcana",
            "arcana_above": "arcana__gte",
            "arcana_below": "arcana__lte",
            "athletics": "athletics",
            "athletics_above": "athletics__gte",
            "athletics_below": "athletics__lte",
            "deception": "deception",
            "deception_above": "deception__gte",
            "deception_below": "deception__lte",
            "history": "history",
            "history_above": "history__gte",
            "history_below": "history__lte",
            "insight": "insight",
            "insight_above": "insight__gte",
            "insight_below": "insight__lte",
            "intimidation": "intimidation",
            "intimidation_above": "intimidation__gte",
            "intimidation_below": "intimidation__lte",
            "investigation": "investigation",
            "investigation_above": "investigation__gte",
            "investigation_below": "investigation__lte",
            "medicine": "medicine",
            "medicine_above": "medicine__gte",
            "medicine_below": "medicine__lte",
            "nature": "nature",
            "nature_above": "nature__gte",
            "nature_below": "nature__lte",
            "perception": "perception",
            "perception_above": "perception__gte",
            "perception_below": "perception__lte",
            "performance": "performance",
            "performance_above": "performance__gte",
            "performance_below": "performance__lte",
            "persuasion": "persuasion",
            "persuasion_above": "persuasion__gte",
            "persuasion_below": "persuasion__lte",
            "religion": "religion",
            "religion_above": "religion__gte",
            "religion_below": "religion__lte",
            "sleight_of_hand": "sleight_of_hand",
            "sleight_of_hand_above": "sleight_of_hand__gte",
            "sleight_of_hand_below": "sleight_of_hand__lte",
            "stealth": "stealth",
            "stealth_above": "stealth__gte",
            "stealth_below": "stealth__lte",
            "survival": "survival",
            "survival_above": "survival__gte",
            "survival_below": "survival__lte"
        },
        "Physical Attack": {
            "name": "name__icontains",
            "damage_type": "damage_type__iexact",
            "dice_type": "dice_type__iexact",
            "dice_count": "dice_count",
            "dice_count_above": "dice_count__gte",
            "dice_count_below": "dice_count__lte",
        },
        "Combat Info": {
            "armor_class": "armor_class",
            "armor_class_above": "armor_class__gte",
            "armor_class_below": "armor_class__lte",
            "initiative": "initiative",
            "initiative_above": "initiative__gte",
            "initiative_below": "initiative__lte",
            "speed": "speed",
            "speed_above": "speed__gte",
            "speed_below": "speed__lte",
            "total_hit_points": "total_hit_points",
            "total_hit_points_above": "total_hit_points__gte",
            "total_hit_points_below": "total_hit_points__lte",
            "current_hit_points": "current_hit_points",
            "current_hit_points_above": "current_hit_points__gte",
            "current_hit_points_below": "current_hit_points__lte",
            "temporary_hit_points": "temporary_hit_points",
            "temporary_hit_points_above": "temporary_hit_points__gte",
            "temporary_hit_points_below": "temporary_hit_points__lte",
            "hit_dice_total": "hit_dice_total",
            "hit_dice_total_above": "hit_dice_total__gte",
            "hit_dice_total_below": "hit_dice_total__lte",
            "hit_dice": "hit_dice__iexact",
            "death_save_success": "death_save_success",
            "death_save_success_above": "death_save_success__gte",
            "death_save_success_below": "death_save_success__lte",
            "death_save_failure": "death_save_failure",
            "death_save_failure_above": "death_save_failure__gte",
            "death_save_failure_below": "death_save_failure__lte",
        }
    }

    fields = model_field_lookup[model]
    query_dict = {}

    for key, value in query_params.items():
        query_dict.update({fields[key]: value})

    return query_dict


def get_default_response(status_code):
    """
    Retrieve a default response object that can be modified as needed
    :param status_code: the HTTP status code (string)
    :return: Rest Framework Response object
    """
    if status_code in RESPONSES:
        return Response(data=copy.copy(RESPONSES[status_code]), status=copy.copy(STATUS_CODES[status_code]))
    else:
        raise NameError('The status code {} not supported.'.format(status_code))
