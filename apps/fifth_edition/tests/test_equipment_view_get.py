from apps.fifth_edition.models import Equipment, PhysicalAttack, PhysicalDefense, AbilityScore
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint
import datetime, random


class TestEquipmentViewGET(TestCase):
    """
    Test class to verify functionality of the EquipmentViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        abilityscore_data = {
            "strength": 30,
            "dexterity": 15,
            "constitution": 27,
            "intelligence": 20,
            "wisdom": 18,
            "charisma": 16
        }

        AbilityScore.objects.create(**abilityscore_data)

        physical_attack_data = {
                "ability_score": AbilityScore.objects.first(),
                "name": "Test Attack 1",
                "damage_type": "bl",
                "dice_type": "d4",
                "dice_count": 1
            }
        
        PhysicalAttack.objects.create(**physical_attack_data)

        physical_defense_data = {
                "defensetype": "Heavy",
                "name": "Test Name",
                "ac": randint(0, 15),
                "strength": randint(0, 15),
                "stealth": "Advantage"
            }

        PhysicalDefense.objects.create(**physical_defense_data)

        # Create a set of Equipment, with varying data
        equipment_data = {
            "name": "Test Equipment",
            "cost": randint(1, 30),
            "weight": random.uniform(1.0, 30.0),
            "description": "Test Description",
            "type": "Weapon",
            "physical_attack": PhysicalAttack.objects.first(),
            "physical_defense": PhysicalDefense.objects.first()
        }

        Equipment.objects.create(**equipment_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_equipment_get_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/equipment", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]

        self.assertEqual(len(results), 1)
        self.assertIn("name", results[0])
        self.assertIn("cost", results[0])
        self.assertIn("weight", results[0])
        self.assertIn("description", results[0])
        self.assertIn("type", results[0])
        self.assertIn("physical_attack", results[0])
        self.assertIn("physical_defense", results[0])
