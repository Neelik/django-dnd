from apps.fifth_edition.models import AbilityScore, Spellcasting
from django.test import TestCase
from rest_framework.test import APIClient


class TestSpellcastingViewGET(TestCase):
    """
    Test class to verify functionality of the SpellcastingViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """
        score_data = {
            "strength": 30,
            "dexterity": 15,
            "constitution": 27,
            "intelligence": 20,
            "wisdom": 18,
            "charisma": 16
        }
        AbilityScore.objects.create(**score_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        AbilityScore.objects.all().delete()
        Spellcasting.objects.all().delete()

    def test_spellcasting_view_get_successful_intelligence_ability(self):
        """
        Unit test to verify that a well-formed GET works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Int")
        response = client.get("/api/ability-scores/{}/spellcasting".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("id", results[0])
        self.assertIn("ability_score", results[0])
        self.assertIn("spellcasting_ability", results[0])
        self.assertEqual(results[0]["spellcasting_ability"], "Int")
        self.assertIn("spell_save", results[0])
        self.assertEqual(results[0]["spell_save"], 13)
        self.assertIn("spell_attack", results[0])
        self.assertEqual(results[0]["spell_attack"], 5)

    def test_spellcasting_view_get_successful_wisdom_ability(self):
        """
        Unit test to verify that a well-formed GET works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Wis")
        response = client.get("/api/ability-scores/{}/spellcasting".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("id", results[0])
        self.assertIn("ability_score", results[0])
        self.assertIn("spellcasting_ability", results[0])
        self.assertEqual(results[0]["spellcasting_ability"], "Wis")
        self.assertIn("spell_save", results[0])
        self.assertEqual(results[0]["spell_save"], 12)
        self.assertIn("spell_attack", results[0])
        self.assertEqual(results[0]["spell_attack"], 4)

    def test_spellcasting_view_get_successful_charisma_ability(self):
        """
        Unit test to verify that a well-formed GET works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Cha")
        response = client.get("/api/ability-scores/{}/spellcasting".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("id", results[0])
        self.assertIn("ability_score", results[0])
        self.assertIn("spellcasting_ability", results[0])
        self.assertEqual(results[0]["spellcasting_ability"], "Cha")
        self.assertIn("spell_save", results[0])
        self.assertEqual(results[0]["spell_save"], 11)
        self.assertIn("spell_attack", results[0])
        self.assertEqual(results[0]["spell_attack"], 3)

    def test_spellcasting_view_get_invalid_ability_score(self):
        """
        Unit test to verify that a malformed GET works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores/9999/spellcasting", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 0)

    def test_spellcasting_view_get_spell_attack_only(self):
        """
        Unit test to verify that retrieving only the spell_attack works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Cha")
        response = client.get("/api/ability-scores/{}/spellcasting?field=attack".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("id", results[0])
        self.assertNotIn("ability_score", results[0])
        self.assertNotIn("spellcasting_ability", results[0])
        self.assertNotIn("spell_save", results[0])
        self.assertIn("spell_attack", results[0])
        self.assertEqual(results[0]["spell_attack"], 3)

    def test_spellcasting_view_get_spell_save_only(self):
        """
        Unit test to verify that retrieving only the spell_attack works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        Spellcasting.objects.create(ability_score=ability_score, spellcasting_ability="Cha")
        response = client.get("/api/ability-scores/{}/spellcasting?field=spell_save".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("id", results[0])
        self.assertNotIn("ability_score", results[0])
        self.assertNotIn("spellcasting_ability", results[0])
        self.assertIn("spell_save", results[0])
        self.assertEqual(results[0]["spell_save"], 11)
        self.assertNotIn("spell_attack", results[0])
