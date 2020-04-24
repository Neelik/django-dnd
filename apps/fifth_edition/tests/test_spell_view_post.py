from apps.fifth_edition.models import Spell
from django.test import TestCase
from rest_framework.test import APIClient
import datetime
from random import randint

class TestSpellViewPOST(TestCase):
    """
    Test class to verify functionality of the Spell ViewPOST API view.
    """

    def test_spell_post_successful(self):
        """
        Test to verify we can successfully create a new Spell object

        :return: None
        """
        client = APIClient()
        spell_data = {
            "casting_time": "00:10:05",
            "spell_range": 10,
            "components": "S, V",
            "duration": "01:10:00",
            "level": 5,
            "name": "Test Spell",
            "desc": "Test Spell Description",
            "magic_school": "Illusion"
        }

        response = client.post("/api/spell/create/", data=spell_data, format="json")
        self.assertEqual(response.status_code, 201)

 