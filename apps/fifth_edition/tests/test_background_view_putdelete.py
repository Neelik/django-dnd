from apps.fifth_edition.models import Background
from django.test import TestCase
from rest_framework.test import APIClient


class TestBackgroundViewPUTDELETE(TestCase):
    """
    Test class to verify functionality of the BackgroundViewPUT API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """
        background_data = {
            "id": "1",
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        Background.objects.create(**background_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_background_put_does_exist(self):
        """
        Unit test to check for a 200 response on a valid request

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background/put-delete/1/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

    def test_background_put_does_not_exist(self):
        """
        Unit test to verify that an invalid request returns a 404

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background/put-delete/99/", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 404)

    def test_background_put_single_value(self):
        """
        Unit test to verify a single value change using PUT

        :return: None
        """
        background = Background.objects.get(id=1)
        client = APIClient()
        update_data = {
            "name": "Sir Fancypants",
            "spec": background.spec,
            "feature": background.feature,
            "alt_feature": background.alt_feature,
            "traits": background.traits,
            "ideals": background.ideals,
            "bonds": background.bonds,
            "flaws": background.flaws,
            "equipment": background.equipment,
        }
        response = client.put("/api/background/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        background = Background.objects.get(id=1)
        self.assertEqual(background.name, "Sir Fancypants")

    def test_background_put_multi_value(self):
        """
        Unit test to verify a multi-value change using PUT

        :return: None
        """

        background = Background.objects.get(id=1)
        client = APIClient()
        update_data = {
            "name": "Sir Fancypants",
            "spec": background.spec,
            "feature": background.feature,
            "alt_feature": background.alt_feature,
            "traits": "He likes super fancy pants.",
            "ideals": background.ideals,
            "bonds": background.bonds,
            "flaws": "Easily distracted by pants.",
            "equipment": background.equipment,
        }
        response = client.put("/api/background/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        background = Background.objects.get(id=1)
        self.assertEqual(background.name, "Sir Fancypants")
        self.assertEqual(background.traits, "He likes super fancy pants.")
        self.assertEqual(background.flaws, "Easily distracted by pants.")

    def test_background_put_id_immutable(self):
        """
        Unit test to verify the id cannot be changed

        :return: None
        """
        background = Background.objects.get(id=1)
        client = APIClient()
        update_data = {
            "id": 99,
            "name": "Sir Fancypants",
            "spec": background.spec,
            "feature": background.feature,
            "alt_feature": background.alt_feature,
            "traits": "He likes super fancy pants.",
            "ideals": background.ideals,
            "bonds": background.bonds,
            "flaws": "Easily distracted by pants.",
            "equipment": background.equipment,
        }
        response = client.put("/api/background/put-delete/1/", data=update_data, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)
        background = Background.objects.get(id=1)
        self.assertEqual(background.id, 1)
