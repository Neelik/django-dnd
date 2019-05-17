from django.db import models
from .common import EditMixin, get_ability_score_increase
from django.core.validators import MaxValueValidator, MinValueValidator


class AbilityScore(models.Model):
    """
    Model of ability scores assigned to characters in DnD
    """

    strength = models.PositiveIntegerField(default=1, verbose_name='Strength',
                                           validators=[MaxValueValidator(30), MinValueValidator(1)])

    @property
    def strength_modifier(self):
        return (self.strength - 10) // 2

    dexterity = models.PositiveIntegerField(default=1, verbose_name='Dexterity',
                                            validators=[MaxValueValidator(30), MinValueValidator(1)])

    @property
    def dexterity_modifier(self):
        return (self.dexterity - 10) // 2
    constitution = models.PositiveIntegerField(default=1, verbose_name='Constitution',
                                               validators=[MaxValueValidator(30), MinValueValidator(1)])

    @property
    def constitution_modifier(self):
        return (self.constitution - 10) // 2
    intelligence = models.PositiveIntegerField(default=1, verbose_name='Intelligence',
                                               validators=[MaxValueValidator(30), MinValueValidator(1)])

    @property
    def intelligence_modifier(self):
        return (self.intelligence - 10) // 2
    wisdom = models.PositiveIntegerField(default=1, verbose_name='Wisdom',
                                         validators=[MaxValueValidator(30), MinValueValidator(1)])

    @property
    def wisdom_modifier(self):
        return (self.wisdom - 10) // 2
    charisma = models.PositiveIntegerField(default=1, verbose_name='Charisma',
                                           validators=[MaxValueValidator(30), MinValueValidator(1)])

    @property
    def charisma_modifier(self):
        return (self.charisma - 10) // 2

    def __str__(self):
        return "Str: {}, Dex: {}, Con: {}, Int: {}, Wis: {}, Cha: {}".format(
            self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)


class Alignment(models.Model):
    """
    Model to store information about the various alignments in DnD 5e

    Descriptions pulled from http://easydamus.com/alignment.html

    """
    name = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=16)
    description = models.TextField()

    def __str__(self):
        return "{} - '{}'".format(self.name.capitalize(), self.subtitle.capitalize())

    class Meta:
        verbose_name_plural = "Alignments"


class Character(models.Model):
    """
    Model to store information about a character in DnD 5e
    """

    RACE_CHOICES = (
        ("Dragonborn", "Dragonborn"),
        ("Dwarf", "Dwarf"),
        ("Elf", "Elf"),
        ("Gnome", "Gnome"),
        ("Half Elf", "Half Elf"),
        ("Half Orc", "Half Orc"),
        ("Halfling", "Halfling"),
        ("Human", "Human"),
        ("Tiefling", "Tiefling")
    )

    name = models.CharField(max_length=50, verbose_name='Character Name')
    level = models.IntegerField(default=1, verbose_name='Level')
    character_class = models.CharField(max_length=20, verbose_name='Class')
    background = models.TextField(verbose_name='Background', null=True, blank=True)
    player_name = models.CharField(max_length=50, verbose_name='Players Name')
    race = models.CharField(max_length=20, choices=RACE_CHOICES, verbose_name='Race')
    alignment = models.CharField(max_length=50, verbose_name='Alignment')
    experience_points = models.PositiveIntegerField(default=0, verbose_name='Experience Points')

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        unique_together = ("name", "character_class", "race", "player_name")


class Feat(models.Model):
    """
    Model storing information about the various Feats available in DnD 5e

    All feats are from Official WotC materials only

    """
    name = models.CharField(max_length=32)
    description = models.TextField()
    prerequisite = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Feats"


class Language(models.Model):
    """
    Model storing information about the various languages available in DnD 5e

    """
    name = models.CharField(max_length=12)
    speakers = models.CharField(max_length=64)
    script = models.CharField(max_length=8, default="---")
    exotic = models.BooleanField(default=False)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name_plural = "Languages"


class PhysicalAttack(models.Model):
    """
    Model for information related to physical attacks
    """
    DAMAGE_TYPE_CHOICES = (
        ("bl", "Bludgeoning"),
        ("pi", "Piercing"),
        ("sl", "Slashing"),
        ("ac", "Acid"),
        ("co", "Cold"),
        ("fi", "Fire"),
        ("fo", "Force"),
        ("li", "Lightning"),
        ("ne", "Necrotic"),
        ("po", "Poison"),
        ("ps", "Psychic"),
        ("ra", "Radiant"),
        ("th", "Thunder"),
    )

    DICE_TYPE_CHOICES = (
        ("d4", "d4"),
        ("d6", "d6"),
        ("d8", "d8"),
        ("d10", "d10"),
        ("d12", "d12"),
    )

    ability_score = models.ForeignKey(AbilityScore, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    damage_type = models.CharField(max_length=2, choices=DAMAGE_TYPE_CHOICES)
    dice_type = models.CharField(max_length=3, choices=DICE_TYPE_CHOICES)
    dice_count = models.IntegerField(default=1)

    @property
    def str_atk_bonus(self):
        return self.ability_score.strength_modifier

    @property
    def dex_atk_bonus(self):
        return self.ability_score.dexterity_modifier

    def __str__(self):
        return "Name: {} Dice Count: {} Dice Type: {} Damage Type: {}".format(self.name, self.dice_count, self.dice_type, self.damage_type)


class Race(models.Model):
    """
    Model storing information about the various races in DnD 5e

    All races are from official WotC materials only

    """
    SIZE_CHOICES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    )

    name = models.CharField(max_length=64)
    age_range = models.CharField(max_length=12,
                                 help_text="Range for when the races are considered adults. Lower values are accepted.")
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    speed = models.PositiveIntegerField()

    def ability_score_increase(self):
        return get_ability_score_increase(self.name.lower())

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name_plural = "Races"


class Tool(models.Model):
    """
    Model to store information about the various tools available in DnD 5e

    """
    TOOL_SET_CHOICES = (
        ("Artisan's Tools", "Artisan's Tools"),
        ("Gaming Set", "Gaming Set"),
        ("General", "General"),
        ("Musical Instrument", "Musical Instrument")
    )

    cost = models.DecimalField(decimal_places=2, max_digits=10, help_text="Value in gold pieces.")
    name = models.CharField(max_length=32)
    set = models.CharField(max_length=16, choices=TOOL_SET_CHOICES)
    weight = models.DecimalField(decimal_places=2, max_digits=10, help_text="Value in pounds.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tools"


