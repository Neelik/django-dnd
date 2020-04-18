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

class NPCSerializer(serializers.ModelSerializer):
    """
    Serializer class for the NPC model
    """

    class Meta:
        model = models.NPC
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
	"""
	Serializer class for Currency model
	"""

	class Meta:
		model = models.Currency
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


class CombatInfoSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Combat Info model
    """

    class Meta:
        model = models.CombatInfo
        fields = "__all__"


class PhysicalDefenseSerializer(serializers.ModelSerializer):
	"""
	Serializer class for PhysicaDefense model
	"""
	
	class Meta:
		model = models.PhysicalDefense
		fields = "__all__"


class PhysicalAttackSerializer(serializers.ModelSerializer):
    """
    Serializer class for Physical Attack model
    """

    class Meta:
        model = models.PhysicalAttack
        fields = ("id", "ability_score", "name", "weapon_type", "properties", "dice_type", "dice_count", "damage_type", "str_atk_bonus", "dex_atk_bonus")
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
        fields = ("id", "ability_score", "spellcasting_ability", "spell_attack", "spell_save", "spell_slots")
        read_only_fields = ("spell_attack", "spell_save")


class BackgroundSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Background model
    """
    class Meta:
        model = models.Background
        fields = "__all__"


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer class for Save model
    """

    class Meta:
        model = models.Save
        fields = ("ability_score", "str_save", "dex_save", "cons_save", "int_save", "wis_save", "cha_save")
        read_only_fields = ("str_save", "dex_save", "cons_save", "int_save", "wis_save", "cha_save")


class EquipmentSerializer(serializers.ModelSerializer):
	"""
	Serializer class for Equipment model
	"""

	class Meta:
		model = models.Equipment
		fields = "__all__"

class SpellSerializer(serializers.ModelSerializer):
	"""
	Serializer class for Spell model
	"""

	class Meta:
		model = models.Spell
		fields = ("casting_time", "spell_range", "components", "duration", "level", "name", "desc", "magic_school")
