from apps.fifth_edition.models import AbilityScore
from django.test import TestCase
from rest_framework.test import APIClient
from random import randint


class TestAbilityScoreViewGET(TestCase):
    """
    Test class to verify functionality of the AbilityScoreViewGET API view.
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
                    "strength": 15,
                    "dexterity": 15,
                    "constitution": 15,
                    "intelligence": 8,
                    "wisdom": 8,
                    "charisma": 8
                }
            else:
                score_data = {
                    "strength": randint(1, 30),
                    "dexterity": randint(1, 30),
                    "constitution": randint(1, 30),
                    "intelligence": randint(1, 30),
                    "wisdom": randint(1, 30),
                    "charisma": randint(1, 30)
                }
            AbilityScore.objects.create(**score_data)

    def tearDown(self):
        """
        Method to remove extraneous test data generated as a side effect of individual tests

        :return: None
        """
        pass

    def test_ability_score_get_view_no_params_successful(self):
        """
        Unit test to verify that a direct request, with no query parameters works properly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertEqual(len(results), 5)
        self.assertIn("strength_modifier", results[0])
        self.assertIn("dexterity_modifier", results[0])
        self.assertIn("constitution_modifier", results[0])
        self.assertIn("intelligence_modifier", results[0])
        self.assertIn("wisdom_modifier", results[0])
        self.assertIn("charisma_modifier", results[0])

    # STRENGTH UNIT TESTS

    def test_ability_score_get_view_query_by_strength_exact_successful(self):
        """
        Unit test to verify that querying by strength, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?strength=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_fifteen = AbilityScore.objects.filter(strength=15).count()
        self.assertTrue(len(results) == str_fifteen)

    def test_ability_score_get_view_query_by_strength_no_results(self):
        """
        Unit test to verify that querying by a strength that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?strength=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_strength_above_successful(self):
        """
        Unit test to verify that querying by a strength_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?strength_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_gt_fifteen = AbilityScore.objects.filter(strength__gte=15).count()
        self.assertTrue(len(results) == str_gt_fifteen)

    def test_ability_score_get_view_query_by_strength_above_no_results(self):
        """
        Unit test to verify that querying by a strength_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?strength_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_strength_below_successful(self):
        """
        Unit test to verify that querying by a strength_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?strength_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        str_lt_fifteen = AbilityScore.objects.filter(strength__lte=20).count()
        self.assertTrue(len(results) == str_lt_fifteen)

    def test_ability_score_get_view_query_by_strength_below_no_results(self):
        """
        Unit test to verify that querying by a strength_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?strength_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    # DEXTERITY UNIT TESTS
    
    def test_ability_score_get_view_query_by_dexterity_exact_successful(self):
        """
        Unit test to verify that querying by dexterity, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?dexterity=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        dex_fifteen = AbilityScore.objects.filter(dexterity=15).count()
        self.assertTrue(len(results) == dex_fifteen)

    def test_ability_score_get_view_query_by_dexterity_no_results(self):
        """
        Unit test to verify that querying by a dexterity that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?dexterity=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_dexterity_above_successful(self):
        """
        Unit test to verify that querying by a dexterity_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?dexterity_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        dex_gt_fifteen = AbilityScore.objects.filter(dexterity__gte=15).count()
        self.assertTrue(len(results) == dex_gt_fifteen)

    def test_ability_score_get_view_query_by_dexterity_above_no_results(self):
        """
        Unit test to verify that querying by a dexterity_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?dexterity_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_dexterity_below_successful(self):
        """
        Unit test to verify that querying by a dexterity_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?dexterity_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        dex_lt_fifteen = AbilityScore.objects.filter(dexterity__lte=20).count()
        self.assertTrue(len(results) == dex_lt_fifteen)

    def test_ability_score_get_view_query_by_dexterity_below_no_results(self):
        """
        Unit test to verify that querying by a dexterity_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?dexterity_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)
        
    # CONSTITUTION UNIT TESTS
        
    def test_ability_score_get_view_query_by_constitution_exact_successful(self):
        """
        Unit test to verify that querying by constitution, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?constitution=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        con_fifteen = AbilityScore.objects.filter(constitution=15).count()
        self.assertTrue(len(results) == con_fifteen)

    def test_ability_score_get_view_query_by_constitution_no_results(self):
        """
        Unit test to verify that querying by a constitution that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?constitution=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_constitution_above_successful(self):
        """
        Unit test to verify that querying by a constitution_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?constitution_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        con_gt_fifteen = AbilityScore.objects.filter(constitution__gte=15).count()
        self.assertTrue(len(results) == con_gt_fifteen)

    def test_ability_score_get_view_query_by_constitution_above_no_results(self):
        """
        Unit test to verify that querying by a constitution_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?constitution_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_constitution_below_successful(self):
        """
        Unit test to verify that querying by a constitution_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?constitution_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        con_lt_fifteen = AbilityScore.objects.filter(constitution__lte=20).count()
        self.assertTrue(len(results) == con_lt_fifteen)

    def test_ability_score_get_view_query_by_constitution_below_no_results(self):
        """
        Unit test to verify that querying by a constitution_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?constitution_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)
        
    # INTELLIGENCE UNIT TESTS
        
    def test_ability_score_get_view_query_by_intelligence_exact_successful(self):
        """
        Unit test to verify that querying by intelligence, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?intelligence=8", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        int_fifteen = AbilityScore.objects.filter(intelligence=8).count()
        self.assertTrue(len(results) == int_fifteen)

    def test_ability_score_get_view_query_by_intelligence_no_results(self):
        """
        Unit test to verify that querying by a intelligence that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?intelligence=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_intelligence_above_successful(self):
        """
        Unit test to verify that querying by a intelligence_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?intelligence_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        int_gt_fifteen = AbilityScore.objects.filter(intelligence__gte=15).count()
        self.assertTrue(len(results) == int_gt_fifteen)

    def test_ability_score_get_view_query_by_intelligence_above_no_results(self):
        """
        Unit test to verify that querying by a intelligence_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?intelligence_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_intelligence_below_successful(self):
        """
        Unit test to verify that querying by a intelligence_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?intelligence_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        int_lt_fifteen = AbilityScore.objects.filter(intelligence__lte=20).count()
        self.assertTrue(len(results) == int_lt_fifteen)

    def test_ability_score_get_view_query_by_intelligence_below_no_results(self):
        """
        Unit test to verify that querying by a intelligence_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?intelligence_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)
        
    # WISDOM UNIT TESTS
        
    def test_ability_score_get_view_query_by_wisdom_exact_successful(self):
        """
        Unit test to verify that querying by wisdom, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?wisdom=8", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        wis_fifteen = AbilityScore.objects.filter(wisdom=8).count()
        self.assertTrue(len(results) == wis_fifteen)

    def test_ability_score_get_view_query_by_wisdom_no_results(self):
        """
        Unit test to verify that querying by a wisdom that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?wisdom=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_wisdom_above_successful(self):
        """
        Unit test to verify that querying by a wisdom_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?wisdom_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        wis_gt_fifteen = AbilityScore.objects.filter(wisdom__gte=15).count()
        self.assertTrue(len(results) == wis_gt_fifteen)

    def test_ability_score_get_view_query_by_wisdom_above_no_results(self):
        """
        Unit test to verify that querying by a wisdom_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?wisdom_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_wisdom_below_successful(self):
        """
        Unit test to verify that querying by a wisdom_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?wisdom_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        wis_lt_fifteen = AbilityScore.objects.filter(wisdom__lte=20).count()
        self.assertTrue(len(results) == wis_lt_fifteen)

    def test_ability_score_get_view_query_by_wisdom_below_no_results(self):
        """
        Unit test to verify that querying by a wisdom_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?wisdom_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)
        
    # CHARISMA UNIT TESTS
        
    def test_ability_score_get_view_query_by_charisma_exact_successful(self):
        """
        Unit test to verify that querying by charisma, exact, works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?charisma=8", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        cha_fifteen = AbilityScore.objects.filter(charisma=8).count()
        self.assertTrue(len(results) == cha_fifteen)

    def test_ability_score_get_view_query_by_charisma_no_results(self):
        """
        Unit test to verify that querying by a charisma that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?charisma=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_charisma_above_successful(self):
        """
        Unit test to verify that querying by a charisma_above works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?charisma_above=15", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        cha_gt_fifteen = AbilityScore.objects.filter(charisma__gte=15).count()
        self.assertTrue(len(results) == cha_gt_fifteen)

    def test_ability_score_get_view_query_by_charisma_above_no_results(self):
        """
        Unit test to verify that querying by a charisma_above that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?charisma_above=31", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)

    def test_ability_score_get_view_query_by_charisma_below_successful(self):
        """
        Unit test to verify that querying by a charisma_below works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?charisma_below=20", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        cha_lt_fifteen = AbilityScore.objects.filter(charisma__lte=20).count()
        self.assertTrue(len(results) == cha_lt_fifteen)

    def test_ability_score_get_view_query_by_charisma_below_no_results(self):
        """
        Unit test to verify that querying by a charisma_below that doesn't exist works correctly

        :return: None
        """

        client = APIClient()
        response = client.get("/api/ability-scores?charisma_below=0", format="json")

        # Assert status code
        self.assertEqual(response.status_code, 200)

        results = response.data["results"]
        self.assertTrue(len(results) == 0)
