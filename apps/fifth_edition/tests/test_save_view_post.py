from random import randint

from django.test import TestCase
from rest_framework.test import APIClient

from apps.fifth_edition.models import AbilityScore, Save


class TestSaveViewPOST(TestCase):
    """
    Test class to verify functionality of the SaveViewPOST API view.
    """

    def setUp(self):
        """
        Creates required data for the tests
        :return: None
        """
        # score_data = {
        #     "strength": 30,
        #     "dexterity": 30,
        #     "constitution": 30,
        #     "intelligence": 30,
        #     "wisdom": 30,
        #     "charisma": 30
        # }
        for num in range(10):
            if num == 0:
                score_data = {
                    "strength": 30,
                    "dexterity": 30,
                    "constitution": 30,
                    "intelligence": 30,
                    "wisdom": 30,
                    "charisma": 30
                }
            else:
                score_data = {
                    "strength": randint(1, 30),
                    "dexterity": randint(1, 30),
                    "constitution": randint(1, 30),
                    "intelligence": randint(1, 30),
                    "wisdom": randint(1, 30),
                    "charisma": randint(1, 30)
                }
            AbilityScore.objects.create(**score_data)

    def test_save_post_can_post(self):
        """
        Test to verify a valid post will go through

        :return: None
        """
        client = APIClient()

        for score in AbilityScore.objects.all():
            new_save = {
                "ability_score": score.id
            }
            response = client.post("/api/save/create/", data=new_save, format="json")
            self.assertEqual(response.status_code, 201)

    def test_save_cant_post(self):
        """
        Test to verify a post with a non-existent ability score will fail
        :return: None
        """
        client = APIClient()
        new_save = {
            "ability_score": 40292
        }

        response = client.post("/api/save/create/", data=new_save, format="json")
        self.assertEqual(response.status_code, 400)

    def test_save_double_post(self):
        """
        Test to verify that a two posts cannot occur for the same ability score entry
        :return: None
        """

        client = APIClient()
        new_save = {
            "ability_score": AbilityScore.objects.first().id
        }

        response = client.post("/api/save/create/", data=new_save, format="json")
        self.assertEqual(response.status_code, 201)
        # Ensures that the relationship is OneToOne
        response = client.post("/api/save/create/", data=new_save, format="json")
        self.assertEqual(response.status_code, 400)

    def test_save_cannot_update_field(self):
        """
        Test to verify that passing a value for a specific save will not assign that value, as it should be derived.
        :return: None
        """
        client = APIClient()
        new_save = {
            "ability_score": AbilityScore.objects.first().id,
            "str_save": 8
        }

        response = client.post("/api/save/create/", data=new_save, format="json")
        self.assertEqual(response.status_code, 201)
        save = Save.objects.first()
        self.assertNotEqual(8, save.str_save)

    def test_save_ignore_extra_fields(self):
        """
        Test that any extra data in the request parameters is ignored except 'ability_score' field.
        :return: None
        """
        client = APIClient()
        new_save = {
            "ability_score": AbilityScore.objects.first().id,
            "junk_data": 5242,
            "more_garbage": "garbage data"
        }

        response = client.post("/api/save/create/", data=new_save, format="json")
        self.assertEqual(response.status_code, 201)
