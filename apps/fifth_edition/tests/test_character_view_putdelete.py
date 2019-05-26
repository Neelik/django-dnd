from apps.fifth_edition.models import Character
from django.test import TestCase
from rest_framework.test import APIClient


class TestCharacterViewPUTDELETE(TestCase):
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
                "id": num,
                "name": "Character {}".format(num),
                "level": num * 2,
                "character_class": class_lookup[num],
                "player_name": "Player {}".format(num),
                "race": race_lookup[num],
                "alignment": "Chaotic Good",
                "experience_points": 10

            }
            Character.objects.create(**character_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass


    def test_character_put_does_exist(self):
        """
        Unit test to check for a 200 response on a valid request

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters/put-delete/1/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

    def test_character_put_does_not_exist(self):
        """
        Unit test to verify that an invalid request returns a 404

        :return: None
        """

        client = APIClient()
        response = client.get("/api/characters/put-delete/99/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 404)

    def test_character_put_single_value(self):
        """
        Unit test to verify a single value change using PUT

        :return: None
        """
        character = Character.objects.get(id=1)
        client = APIClient()
        update_data = {
            "name": character.name,
            "level": 99,
            "character_class": character.character_class,
            "background": character.background,
            "player_name": character.player_name,
            "race": character.race,
            "alignment": character.alignment,
            "experience_points": character.experience_points

        }
        response = client.put("/api/characters/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        character = Character.objects.get(id=1)
        self.assertEqual(character.level, 99)

    def test_character_put_multi_value(self):
        """
        Unit test to verify a multi-value change using PUT

        :return: None
        """

        character = Character.objects.get(id=1)
        client = APIClient()
        update_data = {
            "name": character.name,
            "level": 100,
            "character_class": character.character_class,
            "background": character.background,
            "player_name": character.player_name,
            "race": character.race,
            "alignment": character.alignment,
            "experience_points": 1

        }
        response = client.put("/api/characters/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        character = Character.objects.get(id=1)
        self.assertEqual(character.level, 100)
        self.assertEqual(character.experience_points, 1)

    def test_character_put_id_immutable(self):
        """
        Unit test to verify the id cannot be changed

        :return: None
        """
        character = Character.objects.get(id=1)
        client = APIClient()
        update_data = {
            "id": 99,
            "name": character.name,
            "level": 100,
            "character_class": character.character_class,
            "background": character.background,
            "player_name": character.player_name,
            "race": character.race,
            "alignment": character.alignment,
            "experience_points": 1
        }
        response = client.put("/api/characters/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        character = Character.objects.get(id=1)
        self.assertEqual(character.id, 1)
