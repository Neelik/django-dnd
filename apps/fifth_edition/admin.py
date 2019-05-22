from apps.fifth_edition import models as models
from django.contrib import admin


class BackgroundAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name", "spec", "feature", "alt_feature", "traits", "ideals", "bonds", "flaws", "equipment")


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "level", "character_class", "race")
    search_fields = ("name", "level", "character_class", "race", "player_name")
    readonly_fields = ("id",)


class PhysicalAttackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'damage_type')
    search_fields = ("name", "damage_type")


class SaveAdmin(admin.ModelAdmin):
    list_display = ("id", "ability_score")


class SkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "ability_score")


class SpellcastingAdmin(admin.ModelAdmin):
    list_display = ("id", "ability_score", "spellcasting_ability")
    search_fields = ("spellcasting_ability",)


# Register your models here.
admin.site.register(models.Background, BackgroundAdmin)
admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.PhysicalAttack, PhysicalAttackAdmin)
admin.site.register(models.Save, SaveAdmin)
admin.site.register(models.Skills, SkillsAdmin)
admin.site.register(models.Spellcasting, SpellcastingAdmin)
