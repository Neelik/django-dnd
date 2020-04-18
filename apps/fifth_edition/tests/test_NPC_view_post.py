from apps.fifth_edition.models import NPC
from django.test import TestCase
from rest_framework.test import APIClient
import datetime
from random import randint

class TestNPCViewPOST(TestCase):
    """
    Test class to verify functionality of the NPC ViewPOST API view.
    """

    def test_NPC_post_successful(self):
        """
        Test to verify we can successfully create a new NPC object

        :return: None
        """
        client = APIClient()

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

        NPC_data = {
            "name": "NPC 1",
                "level": 10,
                "npc_class": class_lookup[1],
                "background": "Test Background",
                "race": race_lookup[1],
                "alignment": "Chaotic Good",
        }

        response = client.post("/api/NPC/create/", data=NPC_data, format="json")
        self.assertEqual(response.status_code, 201)

 