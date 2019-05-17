from apps.fifth_edition import models as models
from django.contrib import admin


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "level", "character_class", "race")
    search_fields = ("name", "level", "character_class", "race", "player_name")
    readonly_fields = ("id",)


class PhysicalAttackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'damage_type')
    search_fields = ("name", "damage_type")


# Register your models here.
admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.PhysicalAttack, PhysicalAttackAdmin)