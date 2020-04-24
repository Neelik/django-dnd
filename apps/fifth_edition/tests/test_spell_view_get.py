from apps.fifth_edition.models import Spell
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint
import datetime


class TestSpellViewGET(TestCase):
    """
    Test class to verify functionality of the SpellViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        for num in range(1, 6):
            if num == 1:
                spell_data = {
                    "casting_time": datetime.timedelta(days = 0, minutes = 10, seconds = 30),
                    "spell_range": 15,
                    "components": "S, V",
                    "duration": datetime.timedelta(days = 1, minutes = 0, seconds = 0),
                    "level": 17,
                    "name": "Test Spell",
                    "desc": "Test Spell Description",
                    "magic_school": "illusion"
                }
            else:
                spell_data = {
                    "casting_time": datetime.timedelta(days = randint(0, 365), minutes = randint(0, 59), seconds = randint(0, 59)),
                    "spell_range": randint(1, 30),
                    "components": "S, V",
                    "duration": datetime.timedelta(days = randint(0, 365), minutes = randint(0, 59), seconds = randint(0, 59)),
                    "level": randint(0, 9),
                    "name": "Test Spell",
                    "desc": "Test Spell Description",
                    "magic_school": "illusion"
                }

            Spell.objects.create(**spell_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_spell_get_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/spell", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 5)
        self.assertIn("casting_time", results[0])
        self.assertIn("spell_range", results[0])
        self.assertIn("components", results[0])
        self.assertIn("duration", results[0])
        self.assertIn("level", results[0])
        self.assertIn("name", results[0])
        self.assertIn("desc", results[0])
        self.assertIn("magic_school", results[0])
