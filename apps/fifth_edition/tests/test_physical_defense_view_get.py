from apps.fifth_edition.models import PhysicalDefense
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint
import datetime


class TestPhysicalDefenseViewGET(TestCase):
    """
    Test class to verify functionality of the PhysicalDefenseViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        pd_data = {
            "defensetype": "Heavy",
            "name": "Test Name",
            "ac": randint(0, 15),
            "strength": randint(0, 15),
            "stealth": "Advantage"
        }

        PhysicalDefense.objects.create(**pd_data)

    def test_spell_get_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/physical-defense", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("defensetype", results[0])
        self.assertIn("name", results[0])
        self.assertIn("ac", results[0])
        self.assertIn("strength", results[0])
        self.assertIn("stealth", results[0])

    def test_spell_get_correct(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/physical-defense", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertEqual("Heavy", results[0]["defensetype"])
        self.assertIn("Test Name", results[0]["name"])
        self.assertIn("Advantage", results[0]["stealth"])
