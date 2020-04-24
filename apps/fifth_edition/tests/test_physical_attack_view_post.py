from apps.fifth_edition.models import AbilityScore, PhysicalAttack
from django.test import TestCase
from rest_framework.test import APIClient


class TestPhysicalAttackViewPOST(TestCase):
	"""
	Test class to verify functionality of the PhysicalAttackViewPOST API view.
	"""

	def setUp(self):
		"""
		Method to create prerequisite test information

		:return: None
		"""
		score_data = {
			"strength": 12,
			"dexterity": 15,
			"constitution": 15,
			"intelligence": 14,
			"wisdom": 16,
			"charisma": 18
		}
		AbilityScore.objects.create(**score_data)

	def test_physical_attack_post_succesful(self):
		"""
		Test to verify that a new physical attack entry can be created
		:return: None
		"""
		client = APIClient()
		test_data = {
			"ability_score": AbilityScore.objects.first().id,
			"name": "Test Attack",
			"weapon_type": "Simple Melee Weapon",
			"properties": "Finesse, light, thrown (range 20/60)",
			"dice_type": "d4",
			"dice_count": 2,
			"damage_type": "bl",
			"str_atk_bonus": 1,
			"dex_atk_bonus": 2
		}

		response = client.post("/api/physical-attack/create/", test_data, format="json")
		self.assertEqual(response.status_code, 201)
		entry = PhysicalAttack.objects.first()
		self.assertEqual(entry.name, "Test Attack")
		self.assertEqual(entry.damage_type, "bl")
		self.assertEqual(entry.dice_type, "d4"),
		self.assertEqual(entry.dice_count, 2)
		self.assertEqual(entry.str_atk_bonus, 1)
		self.assertEqual(entry.dex_atk_bonus, 2)

	def test_physical_attack_post_dice_count_default(self):
		"""
		Test to verify that a new physical attack entry can be created
		:return: None
		"""
		client = APIClient()
		test_data = {
			"ability_score": AbilityScore.objects.first().id,
			"name": "Test Attack",
			"weapon_type": "Simple Melee Weapon",
			"properties": "Finesse, light, thrown (range 20/60)",
			"dice_type": "d4",
			"dice_count": 1,
			"damage_type": "bl",
			"str_atk_bonus": 1,
			"dex_atk_bonus": 2
		}

		response = client.post("/api/physical-attack/create/", test_data, format="json")
		self.assertEqual(response.status_code, 201)
		entry = PhysicalAttack.objects.first()
		self.assertEqual(entry.name, "Test Attack")
		self.assertEqual(entry.damage_type, "bl")
		self.assertEqual(entry.dice_type, "d4"),
		self.assertEqual(entry.dice_count, 1)
		self.assertEqual(entry.str_atk_bonus, 1)
		self.assertEqual(entry.dex_atk_bonus, 2)

	def test_physical_attack_post_failure_on_damage_type(self):
		"""
		Test to verify that an invalid physical attack entry will fail to be created
		:return: None
		"""
		client = APIClient()
		test_data = {
			"ability_score": AbilityScore.objects.first().id,
			"name": "Test Attack",
			"damage_type": "zd",
			"dice_type": "d4",
			"dice_count": 2
		}

		response = client.post("/api/physical-attack/create/", test_data, format="json")
		self.assertEqual(response.status_code, 400)

	def test_physical_attack_post_failure_on_dice_type(self):
		"""
		Test to verify that an invalid physical attack entry will fail to be created
		:return: None
		"""
		client = APIClient()
		test_data = {
			"ability_score": AbilityScore.objects.first().id,
			"name": "Test Attack",
			"damage_type": "bl",
			"dice_type": "d14",
			"dice_count": 2
		}

		response = client.post("/api/physical-attack/create/", test_data, format="json")
		self.assertEqual(response.status_code, 400)

	def test_physical_attack_post_double_success(self):
		"""
		Test to verify that a new physical attack entry can be created
		:return: None
		"""
		client = APIClient()
		test_data = {
			"ability_score": AbilityScore.objects.first().id,
			"name": "Test Attack",
			"weapon_type": "Simple Melee Weapon",
			"properties": "Finesse, light, thrown (range 20/60)",
			"dice_type": "d4",
			"dice_count": 1,
			"damage_type": "bl",
			"str_atk_bonus": 1,
			"dex_atk_bonus": 2
		}

		response = client.post("/api/physical-attack/create/", test_data, format="json")
		self.assertEqual(response.status_code, 201)
		entry = PhysicalAttack.objects.first()
		self.assertEqual(entry.name, "Test Attack")
		self.assertEqual(entry.damage_type, "bl")
		self.assertEqual(entry.dice_type, "d4"),
		self.assertEqual(entry.dice_count, 1)
		self.assertEqual(entry.str_atk_bonus, 1)
		self.assertEqual(entry.dex_atk_bonus, 2)

		test_data_two = {
			"ability_score": AbilityScore.objects.first().id,
			"name": "Second Attack",
			"weapon_type": "Simple Melee Weapon",
			"properties": "Finesse, light, thrown (range 20/60)",
			"dice_type": "d8",
			"dice_count": 1,
			"damage_type": "ne",
			"str_atk_bonus": 1,
			"dex_atk_bonus": 2
		}
		response = client.post("/api/physical-attack/create/", test_data_two, format="json")
		self.assertEqual(response.status_code, 201)
		entry = PhysicalAttack.objects.last()
		self.assertEqual(entry.name, "Second Attack")
		self.assertEqual(entry.damage_type, "ne")
		self.assertEqual(entry.dice_type, "d8"),
		self.assertEqual(entry.dice_count, 1)
		self.assertEqual(entry.str_atk_bonus, 1)
		self.assertEqual(entry.dex_atk_bonus, 2)
