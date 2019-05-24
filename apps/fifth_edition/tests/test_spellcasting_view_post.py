from apps.fifth_edition.models import AbilityScore, Spellcasting
from django.test import TestCase
from rest_framework.test import APIClient


class TestSpellcastingViewPOST(TestCase):
    """
    Test class to verify functionality of the SpellcastingViewPOST API view.
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
            "intelligence": 14,
            "wisdom": 16,
            "charisma": 18
        }
        AbilityScore.objects.create(**score_data)

    def test_spellcasting_post_ability_intelligence_successful(self):
        """
        Test to post spellcasting data with intelligence as the ability

        :return: None
        """
        client = APIClient()
        data = {
            "ability_score": AbilityScore.objects.first().id,
            "spellcasting_ability": "Int"
        }

        response = client.post("/api/spellcasting/create/", data=data, format="json")
        self.assertEqual(response.status_code, 201)
        entry = Spellcasting.objects.first()
        self.assertEqual(entry.spellcasting_ability, "Int")
        self.assertEqual(entry.spell_save, 10)
        self.assertEqual(entry.spell_attack, 2)

    def test_spellcasting_post_ability_wisdom_successful(self):
        """
        Test to post spellcasting data with wisdom as the ability

        :return: None
        """
        client = APIClient()
        data = {
            "ability_score": AbilityScore.objects.first().id,
            "spellcasting_ability": "Wis"
        }

        response = client.post("/api/spellcasting/create/", data=data, format="json")
        self.assertEqual(response.status_code, 201)
        entry = Spellcasting.objects.first()
        self.assertEqual(entry.spellcasting_ability, "Wis")
        self.assertEqual(entry.spell_save, 11)
        self.assertEqual(entry.spell_attack, 3)

    def test_spellcasting_post_ability_charisma_successful(self):
        """
        Test to post spellcasting data with charisma as the ability

        :return: None
        """
        client = APIClient()
        data = {
            "ability_score": AbilityScore.objects.first().id,
            "spellcasting_ability": "Cha"
        }

        response = client.post("/api/spellcasting/create/", data=data, format="json")
        self.assertEqual(response.status_code, 201)
        entry = Spellcasting.objects.first()
        self.assertEqual(entry.spellcasting_ability, "Cha")
        self.assertEqual(entry.spell_save, 12)
        self.assertEqual(entry.spell_attack, 4)

    def test_spellcasting_post_same_ability_score(self):
        """
        Test to verify that only one ability score per one spellcasting entry and vice versa

        :return: None
        """
        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Int")

        client = APIClient()
        data = {
            "ability_score": ability_score.id,
            "spellcasting_ability": "Cha"
        }

        response = client.post("/api/spellcasting/create/", data=data, format="json")
        self.assertEqual(response.status_code, 400)
