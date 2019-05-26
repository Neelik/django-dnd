from apps.fifth_edition.models import AbilityScore
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint


class TestAbilityScoreViewPUTDELETE(TestCase):
    """
    Test class to verify functionality of the AbilityScoreViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        # Create a set of Ability Scores, with varying data
        for num in range(1, 6):
            if num == 1:
                score_data = {
                    "id": num,
                    "strength": 15,
                    "dexterity": 15,
                    "constitution": 15,
                    "intelligence": 8,
                    "wisdom": 8,
                    "charisma": 8
                }
            else:
                score_data = {
                    "id": num,
                    "strength": randint(1, 30),
                    "dexterity": randint(1, 30),
                    "constitution": randint(1, 30),
                    "intelligence": randint(1, 30),
                    "wisdom": randint(1, 30),
                    "charisma": randint(1, 30)
                }
            AbilityScore.objects.create(**score_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_ability_score_put_does_exist(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores/put-delete/1/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

    def test_ability_score_put_does_not_exist(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores/put-delete/99/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 404)

    def test_ability_score_put_single_value(self):
        """
        Unit test to verify that a single change can be made

        :return: None
        """

        client = APIClient()
        update_data = {
            "strength": 10
        }
        response = client.put("/api/ability-scores/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        ability_score = AbilityScore.objects.get(id=1)
        self.assertEqual(ability_score.strength, 10)

    def test_ability_score_put_multi_value(self):
        """
        Unit test to verify that a multiple part change can be made

        :return: None
        """

        client = APIClient()
        update_data = {
            "strength": 10,
            "charisma": 1
        }
        response = client.put("/api/ability-scores/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        ability_score = AbilityScore.objects.get(id=1)
        self.assertEqual(ability_score.strength, 10)
        self.assertEqual(ability_score.charisma, 1)

    def test_ability_score_put_id_immutable(self):
        """
        Unit test to verify that the id cannot be changed

        :return: None
        """

        client = APIClient()
        update_data = {
            "id": -1
        }
        response = client.put("/api/ability-scores/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        ability_score = AbilityScore.objects.get(id=1)
        self.assertEqual(ability_score.id, 1)
