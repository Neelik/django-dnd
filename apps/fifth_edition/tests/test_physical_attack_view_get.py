from apps.fifth_edition.models import AbilityScore, PhysicalAttack
from django.test import TestCase
from rest_framework.test import APIClient


class TestPhysicalAttackGET(TestCase):
    """
    Test class to verify correct functionality of the PhysicalAttackViewGET API view
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """
        score_data = {
            "strength": 30,
            "dexterity": 15,
            "constitution": 27,
            "intelligence": 20,
            "wisdom": 18,
            "charisma": 16
        }
        AbilityScore.objects.create(**score_data)

        # Create a set of Physical Attacks, with varying data

        for num in range(1, 6):
            if num == 3:
                damage_type = "ne"
                dice_type = "d12"
            else:
                damage_type = "bl"
                dice_type = "d4"

            physical_attack_data = {
                "ability_score": AbilityScore.objects.first(),
                "name": "Test Attack {}".format(num),
                "damage_type": damage_type,
                "dice_type": dice_type,
                "dice_count": num
            }
            PhysicalAttack.objects.create(**physical_attack_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        AbilityScore.objects.all().delete()
        PhysicalAttack.objects.all().delete()

    def test_physical_attack_get_no_params_succeeds(self):
        """
        Method to test that a GET request succeeds as expected
        :return: None
        """

        client = APIClient()
        response = client.get("/api/physical-attack", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 5)
        self.assertIn("name", results[0])
        self.assertIn("ability_score", results[0])
        self.assertIn("damage_type", results[0])
        self.assertIn("dice_type", results[0])
        self.assertIn("dice_count", results[0])
        self.assertIn("str_atk_bonus", results[0])
        self.assertIn("dex_atk_bonus", results[0])

    def test_physical_attack_get_query_by_name_succeeds(self):
        """
        Method to test that retrieving by the name works correctly
        :return:
        """
        client = APIClient()
        response = client.get("/api/physical-attack?name=Test Attack 1", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("name", results[0])
        self.assertEqual(results[0]["name"], "Test Attack 1")
        self.assertNotEqual(results[0]["name"], "Test Attack 3")
        self.assertEqual(1, results[0]["dice_count"])
        self.assertNotEqual(2, results[0]["dice_count"])

    def test_physical_attack_get_query_by_name_contains_succeeds(self):
        """
        Method to test that retrieving by the name works correctly
        :return:
        """
        client = APIClient()
        response = client.get("/api/physical-attack?name=Test", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 5)
        self.assertIn("name", results[0])
        self.assertEqual(results[0]["name"], "Test Attack 1")
        self.assertEqual(results[2]["name"], "Test Attack 3")

    def test_physical_attack_get_query_by_damage_type_succeeds(self):
        """
        Method to test that retrieving by the damage type works correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?damage_type=NE", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("damage_type", results[0])
        self.assertEqual(results[0]["damage_type"], "ne")
        self.assertNotEqual(results[0]["damage_type"], "bl")

    def test_physical_attack_get_query_by_dice_type_succeeds(self):
        """
        Method to test that retrieving by the dice type works correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?dice_type=d12", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("dice_type", results[0])
        self.assertEqual(results[0]["dice_type"], "d12")
        self.assertNotEqual(results[0]["dice_type"], "d4")

    def test_physical_attack_get_query_by_dice_count_succeeds(self):
        """
        Method to test that retrieving by the dice count works correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?dice_count=5", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("dice_count", results[0])
        self.assertEqual(results[0]["dice_count"], 5)
        self.assertNotEqual(results[0]["dice_count"], 2)

    def test_physical_attack_get_query_by_dice_count_above_succeeds(self):
        """
        Method to test that retrieving by the dice count above a target works correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?dice_count_above=3", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 3)
        self.assertIn("dice_count", results[0])
        self.assertEqual(results[0]["dice_count"], 3)
        self.assertEqual(results[1]["dice_count"], 4)
        self.assertEqual(results[2]["dice_count"], 5)
        self.assertNotEqual(results[0]["dice_count"], 2)

    def test_physical_attack_get_query_by_dice_count_below_succeeds(self):
        """
        Method to test that retrieving by the dice count below a target works correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?dice_count_below=3", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 3)
        self.assertIn("dice_count", results[0])
        self.assertEqual(results[0]["dice_count"], 1)
        self.assertEqual(results[1]["dice_count"], 2)
        self.assertEqual(results[2]["dice_count"], 3)
        self.assertNotEqual(results[0]["dice_count"], 4)

    def test_physical_attack_get_query_by_dice_count_fails(self):
        """
        Method to test that retrieving by an invalid dice count fails correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?dice_count=1000", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)
        results = response.data["results"]
        self.assertEqual(len(results), 0)
        response = client.get("/api/physical-attack?dice_count_above=1000", format="json")
        results = response.data["results"]
        self.assertEqual(len(results), 0)
        # Assert status code
        self.assertEqual(response.status_code, 200)
        response = client.get("/api/physical-attack?dice_count_below=0", format="json")
        results = response.data["results"]
        self.assertEqual(len(results), 0)
        # Assert status code
        self.assertEqual(response.status_code, 200)

    def test_physical_attack_get_query_by_dice_type_fails(self):
        """
        Method to test that retrieving by the dice type fails correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?dice_type=d14", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 0)

    def test_physical_attack_get_query_by_damage_type_fails(self):
        """
        Method to test that retrieving by the damage type fails correctly
        :return: None
        """
        client = APIClient()
        response = client.get("/api/physical-attack?damage_type=zm", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 0)

    def test_physical_attack_get_query_by_name_fails(self):
        """
        Method to test that retrieving by the name fails correctly
        :return:
        """
        client = APIClient()
        response = client.get("/api/physical-attack?name=Test Attack 1000", format="json")
        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 0)
