from apps.fifth_edition.models import CombatInfo
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint


class TestCombatInfoViewPUTDELETE(TestCase):
    """
    Test class to verify functionality of the CombatInfoViewPUT API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        # Create a set of Characters, with varying data
        for num in range(1, 6):
            if num == 1:
                score_data = {
                    "id": num,
                    "armor_class": 15,
                    "initiative": 2,
                    "speed": 30,
                    "total_hit_points": 20,
                    "current_hit_points": 17,
                    "temporary_hit_points": 2,
                    "hit_dice_total": 1,
                    "hit_dice": "d8",
                    "death_save_success": 1,
                    "death_save_failure": 2
                }
            else:
                score_data = {
                    "id": num,
                    "armor_class": randint(1, 30),
                    "initiative": randint(1, 30),
                    "speed": randint(1, 30),
                    "total_hit_points": randint(1, 30),
                    "current_hit_points": randint(1, 30),
                    "temporary_hit_points": randint(1, 30),
                    "hit_dice_total": randint(1, 30),
                    "hit_dice": "d8",
                    "death_save_success": randint(1, 30),
                    "death_save_failure": randint(1, 30)
                }

            CombatInfo.objects.create(**score_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_combat_info_put_does_exist(self):
        """
        Unit test to check for a 200 response on a valid request

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info/put-delete/1/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

    def test_combat_info_put_does_not_exist(self):
        """
        Unit test to verify that an invalid request returns a 404

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info/put-delete/99/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 404)

    def test_combat_info_put_single_value(self):
        """
        Unit test to verify a single value change using PUT

        :return: None
        """
        combat_info = CombatInfo.objects.get(id=1)
        client = APIClient()
        update_data = {
            "armor_class": 10,
            "initiative": combat_info.initiative,
            "speed": combat_info.speed,
            "total_hit_points": combat_info.total_hit_points,
            "current_hit_points": combat_info.current_hit_points,
            "temporary_hit_points": combat_info.temporary_hit_points,
            "hit_dice_total": combat_info.hit_dice_total,
            "hit_dice": combat_info.hit_dice,
            "death_save_success": combat_info.death_save_success,
            "death_save_failure": combat_info.death_save_failure,
        }
        response = client.put("/api/combat-info/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        combat_info = CombatInfo.objects.get(id=1)
        self.assertEqual(combat_info.armor_class, 10)

    def test_combat_info_put_multi_value(self):
        """
        Unit test to verify a multi-value change using PUT

        :return: None
        """

        combatinfo = CombatInfo.objects.get(id=1)
        client = APIClient()
        update_data = {
            "armor_class": 10,
            "initiative": combatinfo.initiative,
            "speed": combatinfo.speed,
            "total_hit_points": 20,
            "current_hit_points": combatinfo.current_hit_points,
            "temporary_hit_points": combatinfo.temporary_hit_points,
            "hit_dice_total": 2,
            "hit_dice": combatinfo.hit_dice,
            "death_save_success": combatinfo.death_save_success,
            "death_save_failure": combatinfo.death_save_failure,
        }
        response = client.put("/api/combat-info/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        combatinfo = CombatInfo.objects.get(id=1)
        self.assertEqual(combatinfo.armor_class, 10)
        self.assertEqual(combatinfo.total_hit_points, 20)
        self.assertEqual(combatinfo.hit_dice_total, 2)

    def test_combat_info_put_id_immutable(self):
        """
        Unit test to verify the id cannot be changed

        :return: None
        """
        combatinfo = CombatInfo.objects.get(id=1)
        client = APIClient()
        update_data = {
            "id": 99,
            "armor_class": 10,
            "initiative": combatinfo.initiative,
            "speed": combatinfo.speed,
            "total_hit_points": 20,
            "current_hit_points": combatinfo.current_hit_points,
            "temporary_hit_points": combatinfo.temporary_hit_points,
            "hit_dice_total": 2,
            "hit_dice": combatinfo.hit_dice,
            "death_save_success": combatinfo.death_save_success,
            "death_save_failure": combatinfo.death_save_failure,
        }
        response = client.put("/api/combat-info/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        combatinfo = CombatInfo.objects.get(id=1)
        self.assertEqual(combatinfo.id, 1)
