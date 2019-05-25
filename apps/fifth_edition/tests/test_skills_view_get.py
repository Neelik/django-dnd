from apps.fifth_edition.models import AbilityScore, Skills
from django.test import TestCase
from rest_framework.test import APIClient



class TestSkillsViewGET(TestCase):
    """
    Test class to verify functionality of the SkillsViewGET API view.
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
            "wisdom": 8,
            "charisma": 5
        }
        ability_score = AbilityScore.objects.create(**score_data)
        Skills.objects.create(ability_score=ability_score)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        AbilityScore.objects.all().delete()
        Skills.objects.all().delete()

    def test_skills_get_view_no_params_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        response = client.get("/api/ability-scores/{}/skills".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("acrobatics", results[0])
        self.assertIn("animal_handling", results[0])
        self.assertIn("arcana", results[0])
        self.assertIn("athletics", results[0])
        self.assertIn("deception", results[0])
        self.assertIn("history", results[0])
        self.assertIn("insight", results[0])
        self.assertIn("intimidation", results[0])
        self.assertIn("investigation", results[0])
        self.assertIn("medicine", results[0])
        self.assertIn("nature", results[0])
        self.assertIn("perception", results[0])
        self.assertIn("performance", results[0])
        self.assertIn("persuasion", results[0])
        self.assertIn("religion", results[0])
        self.assertIn("sleight_of_hand", results[0])
        self.assertIn("stealth", results[0])
        self.assertIn("survival", results[0])

    def test_skills_get_view_ability_score_does_not_exist(self):
        """
        Unit test to verify that a direct request, for saves related to an object that does not exist works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        response = client.get("/api/ability-scores/{}/skills".format(99999), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 0)
