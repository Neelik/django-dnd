from apps.fifth_edition.models import AbilityScore, PhysicalAttack, PhysicalDefense, Equipment
from django.test import TestCase
from rest_framework.test import APIClient
import datetime, random
from random import randint

class TestEquipmentViewPOST(TestCase):
    """
    Test class to verify functionality of the Equipment ViewPOST API view.
    """

    def test_equipment_post_successful(self):
        """
        Test to verify we can successfully create a new Equipment object

        :return: None
        """
        client = APIClient()

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
                "ac": 4,
                "strength": 11,
                "stealth": "Advantage"
            }

        PhysicalDefense.objects.create(**physical_defense_data)

        equipment_data = {
            "name": "Test Equipment",
            "cost": 5,
            "weight": 10.2,
            "description": "Test Description",
            "type": "Weapon",
            "physical_attack": PhysicalAttack.objects.first().id,
            "physical_defense": PhysicalDefense.objects.first().id
        }

        response = client.post("/api/equipment/create/", data=equipment_data, format="json")
        self.assertEqual(response.status_code, 201)

 