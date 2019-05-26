from apps.fifth_edition.models import Background
from django.test import TestCase
from rest_framework.test import APIClient


class TestBackgroundViewGET(TestCase):
    """
    Test class to verify functionality of the CharacterViewGET API view.
    """

    def setUp(self):
        """
        Method to create required test data

        :return: None
        """

        # Create a background for testing

        background_data = {
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

    def test_background_get_view_no_params_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("name", results[0])
        self.assertIn("spec", results[0])
        self.assertIn("feature", results[0])
        self.assertIn("alt_feature", results[0])
        self.assertIn("traits", results[0])
        self.assertIn("ideals", results[0])
        self.assertIn("bonds", results[0])
        self.assertIn("flaws", results[0])
        self.assertIn("equipment", results[0])

    def test_background_get_view_query_by_name_successful(self):
        """
        Unit test to verify that querying by name works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background?name=name", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["name"], "name")

    def test_background_get_view_query_by_name_no_results(self):
        """
        Unit test to verify that querying by a name that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background?name=Seal Clubber", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_background_get_view_query_by_spec_successful(self):
        """
        Unit test to verify that querying by spec works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background?spec=spec", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["spec"], "spec")

    def test_background_get_view_query_by_spec_no_results(self):
        """
        Unit test to verify that querying by a spec that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background?spec=Spaceworthyness", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_background_get_view_query_by_equip_successful(self):
        """
        Unit test to verify that querying by equipment works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background?equipment=dagger", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert data in response results, specifically verifying order of objects by level
        results = response.data["results"]
        self.assertTrue(len(results) == 1)
        self.assertEqual(results[0]["equipment"], "dagger")

    def test_background_get_view_query_by_equip_no_results(self):
        """
        Unit test to verify that querying by a equipment that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/background?equipment=tank", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)
