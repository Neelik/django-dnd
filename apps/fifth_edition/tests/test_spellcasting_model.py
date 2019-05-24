from apps.fifth_edition.models import AbilityScore, Spellcasting
from django.test import TestCase


class TestSpellcastingModel(TestCase):
    """
    Test class to verify functionality of the Skills ViewPOST API view.
    """

    def setUp(self):
        """
        Method to create prerequisite test information

        :return: None
        """
        score_data = {
            "strength": 15,
            "dexterity": 15,
            "constitution": 15,
            "intelligence": 8,
            "wisdom": 8,
            "charisma": 8
        }
        AbilityScore.objects.create(**score_data)

    def test_spellcasting_model_new_entry(self):
        """
        Test that creating a new entry works

        :return: None
        """

        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Wis")
        sp_entry = Spellcasting.objects.first()

        self.assertTrue(Spellcasting.objects.count() > 0)
        self.assertEqual(sp_entry.spell_save, ability_score.wisdom_modifier + 8)
        self.assertEqual(sp_entry.spell_attack, ability_score.wisdom_modifier)
