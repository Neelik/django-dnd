from django.test import TestCase
from rest_framework.test import APIClient


class TestCharacterViewPOST(TestCase):
    """
    Test class to verify functionality of the CharacterViewPOST API view.
    """

    def test_character_post_can_post(self):
        """
        Test to verify a valid post will go through with no value for background

        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_character_post_already_posted(self):
        """
        Test to verify a post cannot be made for a character that has already been posted
        Should return error code 409: "Resource already exists"
        :return:
        """

        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        client.post("/api/characters/create/", data=new_character, format="json")

        new_character_two = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character_two, format="json")

        # Assert status code
        # Will return a "non_field_errors" field in the response data, with a code of 400
        self.assertEqual(response.status_code, 400)
        self.assertIn("non_field_errors", response.data)

    def test_character_post_1_of_4_constraints_different_works_name(self):
        """
        Unit test to verify that if 1 of 4 of the constraints fields is different, the creation is allowed

        :return: None
        """
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        client.post("/api/characters/create/", data=new_character, format="json")

        # Changed the name, so it should work
        new_character_two = {
            "name": "Deaven",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character_two, format="json")
        self.assertEqual(response.status_code, 201)

    def test_character_post_1_of_4_constraints_different_works_character_class(self):
        """
        Unit test to verify that if 1 of 4 of the constraints fields is different, the creation is allowed

        :return: None
        """
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        client.post("/api/characters/create/", data=new_character, format="json")

        # Changed the character_class, so it should work
        new_character_two = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Monk",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character_two, format="json")
        self.assertEqual(response.status_code, 201)

    def test_character_post_1_of_4_constraints_different_works_player_name(self):
        """
        Unit test to verify that if 1 of 4 of the constraints fields is different, the creation is allowed

        :return: None
        """
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        client.post("/api/characters/create/", data=new_character, format="json")

        # Changed the player_name, so it should work
        new_character_two = {
            "name": "Deaven",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Gumbo",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character_two, format="json")
        self.assertEqual(response.status_code, 201)

    def test_character_post_1_of_4_constraints_different_works_race(self):
        """
        Unit test to verify that if 1 of 4 of the constraints fields is different, the creation is allowed

        :return: None
        """
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        client.post("/api/characters/create/", data=new_character, format="json")

        # Changed the race, so it should work
        new_character_two = {
            "name": "Deaven",
            "level": 0,
            "character_class": "Rogue",
            "background": "",
            "player_name": "Josh",
            "race": "Human",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character_two, format="json")
        self.assertEqual(response.status_code, 201)

    def test_character_post_can_post_background(self):
        """
        Test to verify a valid post will go through with a value for background

        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_character_post_can_post_background_is_null(self):
        """
        Test to verify a valid post will go through with a null background

        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_character_post_player_name_null(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be null
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_character_class_null(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be null
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_name_null(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be null
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_can_player_name_null(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be null
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_race_null(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be null
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "Josh",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_alignment_null(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be null
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_experience_null(self):
        """
        Test to verify null experience points is a successful post
        :return: None
        """

        # removed player_name field from new_character data set
        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good"
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_character_post_player_name_empty_string(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be an empty string
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Deavenind",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_name_empty_string(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be an empty string
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "",
            "level": 0,
            "character_class": "Rogue",
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_character_class_empty_string(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be an empty string
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Happy",
            "level": 99,
            "character_class": "",
            "background": "Thief",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_race_empty_string(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be an empty string
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Happy",
            "level": 99,
            "character_class": "Rogue",
            "background": "Paladin",
            "player_name": "Josh",
            "race": "",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_alignment_empty_string(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be an empty string
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Happy",
            "level": 99,
            "character_class": "Rogue",
            "background": "Paladin",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_character_post_level_null(self):
        """
        Test to verify a null level value will be a successful post
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Happy",
            "character_class": "Rogue",
            "background": "Paladin",
            "player_name": "Josh",
            "race": "Dragonborn",
            "alignment": "Chaotic good",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_character_post_invalid_race_type(self):
        """
        Test to verify an invalid post will not go through
        e.g. the player_name field will be an empty string
        Should return error code 400: "One or more required fields are missing."
        :return: None
        """

        client = APIClient()
        new_character = {
            "name": "Happy",
            "level": 99,
            "character_class": "Rogue",
            "background": "Paladin",
            "player_name": "Josh",
            "race": "car",
            "alignment": "",
            "experience_points": 0
        }

        response = client.post("/api/characters/create/", data=new_character, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)
