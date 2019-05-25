from django.test import TestCase
from rest_framework.test import APIClient


class TestCombatInfoViewPOST(TestCase):
    """
    Test class to verify functionality of the CombatInfoViewPOST API view.
    """

    def test_CombatInfo_post_can_post(self):
        """
        Test to verify a valid post will go through with all valid values

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_already_posted(self):
        """
        Test to verify a post can be made for the already existing combat info that has already been posted
        Should return error code 201
        :return:
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        client.post("/api/combat-info/create/", data=score_data, format="json")

        combat_info_two = {
            "armor_class": 20,
            "initiative": 54,
            "speed": 22,
            "total_hit_points": 100,
            "current_hit_points": 58,
            "temporary_hit_points": 20,
            "hit_dice_total": 1,
            "hit_dice": "d10",
            "death_save_success": 0,
            "death_save_failure": 0
        }

        response = client.post("/api/combat-info/create/", data=combat_info_two, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_armor(self):
        """
        Test to verify a valid post will go through with all valid values and no armor_class

        :return: None
        """

        client = APIClient()
        score_data = {
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_initiative(self):
        """
        Test to verify a valid post will go through with all valid values and no initiative

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_speed(self):
        """
        Test to verify a valid post will go through with all valid values and no speed

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_total_hit_points(self):
        """
        Test to verify a valid post will go through with all valid values and no total_hit_points

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_current_hit_points(self):
        """
        Test to verify a valid post will go through with all valid values and no current_hit_points

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_temporary_hit_points(self):
        """
        Test to verify a valid post will go through with all valid values and no temporary_hit_points

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_hit_dice_total(self):
        """
        Test to verify a valid post will go through with all valid values and no hit_dice_total

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_cant_post_no_hit_dice(self):
        """
        Test to verify an invalid post doesn't go through with all valid values and no hit_dice

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_CombatInfo_post_can_post_no_death_save_success(self):
        """
        Test to verify a valid post will go through with all valid values and no death_save_success

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_can_post_no_death_save_failure(self):
        """
        Test to verify a valid post will go through with all valid values and no death_save_failure

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_CombatInfo_post_cant_post_invalid_hit_dice(self):
        """
        Test to verify a valid post not go through due to invalid dice type

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d30",
            "death_save_success": 1,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_CombatInfo_post_cant_post_invalid_death_save_success(self):
        """
        Test to verify a valid post not go through due to invalid death save successes

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 5,
            "death_save_failure": 2
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)

    def test_CombatInfo_post_cant_post_invalid_death_save_failure(self):
        """
        Test to verify a valid post not go through due to invalid death save failures

        :return: None
        """

        client = APIClient()
        score_data = {
            "armor_class": 15,
            "initiative": 2,
            "speed": 30,
            "total_hit_points": 20,
            "current_hit_points": 17,
            "temporary_hit_points": 0,
            "hit_dice_total": 1,
            "hit_dice": "d8",
            "death_save_success": 1,
            "death_save_failure": 10
        }

        response = client.post("/api/combat-info/create/", data=score_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 400)
