from apps.fifth_edition.models import CombatInfo
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint


class TestCombatInfoViewGET(TestCase):
    """
    Test class to verify functionality of the CombatInfoViewGET API view.
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

    def test_combat_info_get_info_no_params_successful_except_hit_dice(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 5)
        self.assertIn("armor_class", results[0])
        self.assertIn("initiative", results[0])
        self.assertIn("speed", results[0])
        self.assertIn("total_hit_points", results[0])
        self.assertIn("current_hit_points", results[0])
        self.assertIn("temporary_hit_points", results[0])
        self.assertIn("hit_dice_total", results[0])
        self.assertIn("hit_dice", results[0])
        self.assertIn("death_save_success", results[0])
        self.assertIn("death_save_failure", results[0])

    def test_combat_info_get_info_query_by_armor_class_exact_successful(self):
        """
        Unit test to verify that querying by armor class, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?armor_class=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(armor_class=15).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_armor_class_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by armor class, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?armor_class=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_armor_class_above_successful(self):
        """
        Unit test to verify that querying by a armor_class_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?armor_class_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(armor_class__gte=15).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_armor_class_above_no_results(self):
        """
        Unit test to verify that querying by a armor_class_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?armor_class_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_armor_class_below_successful(self):
        """
        Unit test to verify that querying by a armor_class_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?armor_class_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(armor_class__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_armor_class_below_no_results(self):
        """
        Unit test to verify that querying by a armor_class_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?armor_class_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #initiative
    def test_combat_info_get_info_query_by_initiative_exact_successful(self):
        """
        Unit test to verify that querying by initiative, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?initiative=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(initiative=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_initiative_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by initiative, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?initiative=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_initiative_above_successful(self):
        """
        Unit test to verify that querying by a initiative_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?initiative_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(initiative__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_initiative_above_no_results(self):
        """
        Unit test to verify that querying by a initiative_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?initiative_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_initiative_below_successful(self):
        """
        Unit test to verify that querying by a initiative_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?initiative_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(initiative__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_initiative_below_no_results(self):
        """
        Unit test to verify that querying by a initiative_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?initiative_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #speed
    def test_combat_info_get_info_query_by_speed_exact_successful(self):
        """
        Unit test to verify that querying by speed, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?speed=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(speed=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_speed_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by speed, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?speed=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_speed_above_successful(self):
        """
        Unit test to verify that querying by a speed_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?speed_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(speed__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_speed_above_no_results(self):
        """
        Unit test to verify that querying by a speed_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?speed_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_speed_below_successful(self):
        """
        Unit test to verify that querying by a speed_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?speed_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(speed__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_speed_below_no_results(self):
        """
        Unit test to verify that querying by a speed_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?speed_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #total_hit_points
    def test_combat_info_get_info_query_by_total_hit_points_exact_successful(self):
        """
        Unit test to verify that querying by total_hit_points, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?total_hit_points=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(total_hit_points=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_total_hit_points_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by total_hit_points, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?total_hit_points=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_total_hit_points_above_successful(self):
        """
        Unit test to verify that querying by a total_hit_points_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?total_hit_points_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(total_hit_points__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_total_hit_points_above_no_results(self):
        """
        Unit test to verify that querying by a total_hit_points_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?total_hit_points_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_total_hit_points_below_successful(self):
        """
        Unit test to verify that querying by a total_hit_points_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?total_hit_points_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(total_hit_points__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_total_hit_points_below_no_results(self):
        """
        Unit test to verify that querying by a total_hit_points_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?total_hit_points_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #current_hit_points
    def test_combat_info_get_info_query_by_current_hit_points_exact_successful(self):
        """
        Unit test to verify that querying by current_hit_points, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?current_hit_points=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(current_hit_points=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_current_hit_points_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by current_hit_points, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?current_hit_points=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_current_hit_points_above_successful(self):
        """
        Unit test to verify that querying by a current_hit_points_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?current_hit_points_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(current_hit_points__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_current_hit_points_above_no_results(self):
        """
        Unit test to verify that querying by a current_hit_points_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?current_hit_points_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_current_hit_points_below_successful(self):
        """
        Unit test to verify that querying by a current_hit_points_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?current_hit_points_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(current_hit_points__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_current_hit_points_below_no_results(self):
        """
        Unit test to verify that querying by a current_hit_points_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?current_hit_points_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #temporary_hit_points
    def test_combat_info_get_info_query_by_temporary_hit_points_exact_successful(self):
        """
        Unit test to verify that querying by temporary_hit_points, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?temporary_hit_points=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(temporary_hit_points=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_temporary_hit_points_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by temporary_hit_points, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?temporary_hit_points=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_temporary_hit_points_above_successful(self):
        """
        Unit test to verify that querying by a temporary_hit_points_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?temporary_hit_points_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(temporary_hit_points__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_temporary_hit_points_above_no_results(self):
        """
        Unit test to verify that querying by a temporary_hit_points_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?temporary_hit_points_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_temporary_hit_points_below_successful(self):
        """
        Unit test to verify that querying by a temporary_hit_points_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?temporary_hit_points_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(temporary_hit_points__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_temporary_hit_points_below_no_results(self):
        """
        Unit test to verify that querying by a temporary_hit_points_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?temporary_hit_points_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #hit_dice_total
    def test_combat_info_get_info_query_by_hit_dice_total_exact_successful(self):
        """
        Unit test to verify that querying by hit_dice_total, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?hit_dice_total=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(hit_dice_total=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_hit_dice_total_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by hit_dice_total, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?hit_dice_total=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_hit_dice_total_above_successful(self):
        """
        Unit test to verify that querying by a hit_dice_total_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?hit_dice_total_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(hit_dice_total__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_hit_dice_total_above_no_results(self):
        """
        Unit test to verify that querying by a hit_dice_total_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?hit_dice_total_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_hit_dice_total_below_successful(self):
        """
        Unit test to verify that querying by a hit_dice_total_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?hit_dice_total_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(hit_dice_total__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_hit_dice_total_below_no_results(self):
        """
        Unit test to verify that querying by a hit_dice_total_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?hit_dice_total_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #death_save_success
    def test_combat_info_get_info_query_by_death_save_success_exact_successful(self):
        """
        Unit test to verify that querying by death_save_success, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_success=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(death_save_success=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_death_save_success_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by death_save_success, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_success=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_death_save_success_above_successful(self):
        """
        Unit test to verify that querying by a death_save_success_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_success_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(death_save_success__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_death_save_success_above_no_results(self):
        """
        Unit test to verify that querying by a death_save_success_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_success_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_death_save_success_below_successful(self):
        """
        Unit test to verify that querying by a death_save_success_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_success_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(death_save_success__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_death_save_success_below_no_results(self):
        """
        Unit test to verify that querying by a death_save_success_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_success_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    #death_save_failure
    def test_combat_info_get_info_query_by_death_save_failure_exact_successful(self):
        """
        Unit test to verify that querying by death_save_failure, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_failure=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = CombatInfo.objects.filter(death_save_failure=2).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_combat_info_get_info_query_by_death_save_failure_doesnt_exist_successful(self):
        """
        Unit test to verify that querying by death_save_failure, doesnt exist, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_failure=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_death_save_failure_above_successful(self):
        """
        Unit test to verify that querying by a death_save_failure_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_failure_above=2", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = CombatInfo.objects.filter(death_save_failure__gte=2).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_combat_info_get_info_query_by_death_save_failure_above_no_results(self):
        """
        Unit test to verify that querying by a death_save_failure_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_failure_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_combat_info_get_info_query_by_death_save_failure_below_successful(self):
        """
        Unit test to verify that querying by a death_save_failure_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_failure_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = CombatInfo.objects.filter(death_save_failure__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_combat_info_get_info_query_by_death_save_failure_below_no_results(self):
        """
        Unit test to verify that querying by a death_save_failure_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/combat-info?death_save_failure_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)