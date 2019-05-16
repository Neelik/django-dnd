from apps.fifth_edition import models
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Character model
    """

    class Meta:
        model = models.Character
        fields = "__all__"


class AbilityScoreSerializer(serializers.ModelSerializer):
    """
    Serializer class for the AbilityScore model
    """

    class Meta:
        model = models.AbilityScore
        fields = ("id",
                  "strength", "strength_modifier",
                  "dexterity", "dexterity_modifier",
                  "constitution", "constitution_modifier",
                  "intelligence", "intelligence_modifier",
                  "wisdom", "wisdom_modifier",
                  "charisma", "charisma_modifier")
        read_only_fields = ("strength_modifier", "dexterity_modifier", "constitution_modifier", "intelligence_modifier",
                            "wisdom_modifier", "charisma_modifier")
