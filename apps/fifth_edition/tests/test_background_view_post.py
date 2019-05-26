from django.test import TestCase
from rest_framework.test import APIClient


class TestBackgroundViewPOST(TestCase):
    """
    Test class to verify functionality of the BackgroundViewPOST API view.
    """

    def test_character_post_can_post(self):
        """
        Test to verify a valid post will go through

        :return: None
        """

        client = APIClient()
        new_background = {
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

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_ignores_extra_fields_in_request(self):
        """
        Test that any extra data in the request parameters is ignored.

        :return: None
        """
        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
            "godmode": "on",
            "infiniteammo": "true",
        }
        response = client.post("/api/background/create/", data=new_background, format="json")
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_name_is_empty(self):
        """
        Test to verify a valid post will go through with a empty name

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_spec_is_empty(self):
        """
        Test to verify a valid post will go through with a empty spec

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_feature_is_empty(self):
        """
        Test to verify a valid post will go through with a empty feature

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_alt_feature_is_empty(self):
        """
        Test to verify a valid post will go through with a empty alt_feature

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_traits_is_empty(self):
        """
        Test to verify a valid post will go through with a empty traits

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_ideals_is_empty(self):
        """
        Test to verify a valid post will go through with a empty ideals

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_bonds_is_empty(self):
        """
        Test to verify a valid post will go through with a empty bonds

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_flaws_is_empty(self):
        """
        Test to verify a valid post will go through with a empty flaws

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_equipment_is_empty(self):
        """
        Test to verify a valid post will go through with a empty equipment

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_name_is_null(self):
        """
        Test to verify a valid post will go through with a null name

        :return: None
        """

        client = APIClient()
        new_background = {
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_spec_is_null(self):
        """
        Test to verify a valid post will go through with a null spec

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_feature_is_null(self):
        """
        Test to verify a valid post will go through with a null feature

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_alt_feature_is_null(self):
        """
        Test to verify a valid post will go through with a null alt_feature

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_traits_is_null(self):
        """
        Test to verify a valid post will go through with a null traits

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_ideals_is_null(self):
        """
        Test to verify a valid post will go through with a null ideals

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "bonds": "bonds",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_bonds_is_null(self):
        """
        Test to verify a valid post will go through with a null bonds

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "flaws": "flaws",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_flaws_is_null(self):
        """
        Test to verify a valid post will go through with a null flaws

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "equipment": "dagger",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_equipment_is_null(self):
        """
        Test to verify a valid post will go through with a null equipment

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "name",
            "spec": "spec",
            "feature": "feature",
            "alt_feature": "alt_feature",
            "traits": "traits",
            "ideals": "ideals",
            "bonds": "bonds",
            "flaws": "flaws",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_all_is_null(self):
        """
        Test to verify a valid post will go through with a null equipment

        :return: None
        """

        client = APIClient()
        new_background = {

        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)

    def test_background_post_can_post_all_is_empty(self):
        """
        Test to verify a valid post will go through with a null equipment

        :return: None
        """

        client = APIClient()
        new_background = {
            "name": "",
            "spec": "",
            "feature": "",
            "alt_feature": "",
            "traits": "",
            "ideals": "",
            "bonds": "",
            "flaws": "",
        }

        response = client.post("/api/background/create/", data=new_background, format="json")

        # Assert status code
        self.assertEqual(response.status_code, 201)
