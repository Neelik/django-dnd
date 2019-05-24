from apps.fifth_edition.models import AbilityScore, Save
from django.test import TestCase
from rest_framework.test import APIClient


class TestSaveViewGET(TestCase):
    """
    Test class to verify functionality of the SaveViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        # Create a set of Characters, with varying data
        score_data = {
            "strength": 15,  # +2
            "dexterity": 15,  # +2
            "constitution": 15,  # +2
            "intelligence": 8,  # -1
            "wisdom": 8,  # -1
            "charisma": 8  # -1
        }
        ability_score = AbilityScore.objects.create(**score_data)
        Save.objects.create(ability_score=ability_score)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        AbilityScore.objects.all().delete()
        Save.objects.all().delete()

    def test_save_get_view_no_params_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        response = client.get("/api/ability-scores/{}/saves".format(ability_score.id), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("str_save", results[0])
        self.assertIn("cons_save", results[0])
        self.assertIn("dex_save", results[0])
        self.assertIn("int_save", results[0])
        self.assertIn("wis_save", results[0])
        self.assertIn("cha_save", results[0])

    def test_save_get_view_ability_score_does_not_exist(self):
        """
        Unit test to verify that a direct request, for saves related to an object that does not exist works correctly

        :return: None
        """

        client = APIClient()
        ability_score = AbilityScore.objects.first()
        response = client.get("/api/ability-scores/{}/saves".format(99999), format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 0)
