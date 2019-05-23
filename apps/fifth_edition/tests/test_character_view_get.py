from apps.fifth_edition.models import Character
from django.test import TestCase
from rest_framework.test import APIClient


class TestCharacterViewGET(TestCase):
    """
    Test class to verify functionality of the CharacterViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        class_lookup = {
            1: "Rogue",
            2: "Paladin",
            3: "Cleric",
            4: "Barbarian",
            5: "Warlock"
        }

        race_lookup = {
            1: "Human",
            2: "Dragonborn",
            3: "Dwarf",
            4: "Gnome",
            5: "Tiefling"
        }

        # Create a set of Characters, with varying data
        for num in range(1, 6):
            character_data = {
                "name": "Character {}".format(num),
                "level": num * 2,
                "character_class": class_lookup[num],
                "player_name": "Player {}".format(num),
                "race": race_lookup[num],
                "alignment": "Chaotic Good",

            }
            Character.objects.create(**character_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_character_get_view_no_params_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertEqual(results[0]["level"], 10)
        self.assertEqual(results[-1]["level"], 2)

    def test_character_get_view_query_by_name_successful(self):
        """
        Unit test to verify that querying by name works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?name=Character 1", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["name"], "Character 1")

    def test_character_get_view_query_by_name_no_results(self):
        """
        Unit test to verify that querying by a name that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?name=Character 6", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_character_get_view_query_by_player_successful(self):
        """
        Unit test to verify that querying by player works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?player=Player 1", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["player_name"], "Player 1")

    def test_character_get_view_query_by_player_no_results(self):
        """
        Unit test to verify that querying by a player that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?player=Player 6", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_character_get_view_query_by_class_successful(self):
        """
        Unit test to verify that querying by class works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?class=Warlock", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["character_class"], "Warlock")

    def test_character_get_view_query_by_class_no_results(self):
        """
        Unit test to verify that querying by a class that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?class=Monk", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_character_get_view_query_by_race_successful(self):
        """
        Unit test to verify that querying by race works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?race=Dwarf", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["race"], "Dwarf")

    def test_character_get_view_query_by_race_no_results(self):
        """
        Unit test to verify that querying by a race that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?race=Half Orc", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_character_get_view_query_by_level_above_successful(self):
        """
        Unit test to verify that querying by level_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?level_above=9", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["level"], 10)

    def test_character_get_view_query_by_level_above_no_results(self):
        """
        Unit test to verify that querying by a level_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?level_above=11", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_character_get_view_query_by_level_below_successful(self):
        """
        Unit test to verify that querying by level_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?level_below=3", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["level"], 2)

    def test_character_get_view_query_by_level_below_no_results(self):
        """
        Unit test to verify that querying by a level_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters?level_below=1", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 0)
