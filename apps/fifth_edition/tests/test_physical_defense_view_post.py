from apps.fifth_edition.models import PhysicalDefense
from django.test import TestCase
from rest_framework.test import APIClient
import datetime
from random import randint

class TestPhysicalDefenseViewPOST(TestCase):
    """
    Test class to verify functionality of the PhysicalDefense ViewPOST API view.
    """

    def test_physical_defense_post_successful(self):
        """
        Test to verify we can successfully create a new PhysicalDefense object

        :return: None
        """
        client = APIClient()
        pd_data = {
            "defensetype": "Heavy",
            "name": "Test Name",
            "ac": randint(0, 15),
            "strength": randint(0, 15),
            "stealth": "Advantage"
        }

        response = client.post("/api/physical-defense/create/", data=pd_data, format="json")
        self.assertEqual(response.status_code, 201)

 