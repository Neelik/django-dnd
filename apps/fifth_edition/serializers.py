from apps.fifth_edition import models
from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


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


class PhysicalAttackSerializer(serializers.ModelSerializer):
    """
    Serializer class for Physical Attack model
    """

    class Meta:
        model = models.PhysicalAttack
        fields = ("id", "ability_score", "name", "damage_type", "dice_type", "dice_count", "str_atk_bonus", "dex_atk_bonus")
        read_only_fields = ("str_atk_bonus", "dex_atk_bonus")


class SkillsSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Skills model
    """

    class Meta:
        model = models.Skills
        fields = ("id", "acrobatics", "animal_handling", "arcana", "athletics", "deception", "history", "insight",
                  "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion",
                  "religion", "sleight_of_hand", "stealth", "survival", "ability_score")
        read_only_fields = ("acrobatics", "animal_handling", "arcana", "athletics", "deception", "history", "insight",
                  "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion",
                  "religion", "sleight_of_hand", "stealth", "survival")


class SpellcastingSerializer(DynamicFieldsModelSerializer):
    """
    Serializer class for Spellcasting model
    """

    class Meta:
        model = models.Spellcasting
        fields = ("id", "ability_score", "spellcasting_ability", "spell_attack", "spell_save")
        read_only_fields = ("spell_attack", "spell_save")