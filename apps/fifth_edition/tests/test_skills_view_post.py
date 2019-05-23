from apps.fifth_edition.models import AbilityScore, Skills
from django.test import TestCase
from rest_framework.test import APIClient


class TestSkillsViewPOST(TestCase):
    """
    Test class to verify functionality of the Skills ViewPOST API view.
    """

    def setUp(self):
        """
        Method to create prerequisite test information

        :return: None
        """
        score_data = {
            "strength": 15,
            "dexterity": 15,
            "constitution": 15,
            "intelligence": 8,
            "wisdom": 8,
            "charisma": 8
        }
        AbilityScore.objects.create(**score_data)

    def test_skills_post_can_post(self):
        """
        Test to verify we can successfully create a new Skills object

        :return: None
        """

        client = APIClient()
        skills_data = {
            "ability_score": AbilityScore.objects.first().id
        }

        response = client.post("/api/skills/create/", data=skills_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_skills_post_invalid_relationship(self):
        """
        Test to verify that if an ID for an invalid AbilityScore object is provided, the endpoint fails

        :return: None
        """
        client = APIClient()
        skills_data = {
            "ability_score": 99999
        }

        response = client.post("/api/skills/create/", data=skills_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_skills_cannot_update_a_field(self):
        """
        Test to verify that passing a value for a specific skill will not assign that value, as it should be derived.

        :return: None
        """
        client = APIClient()
        skills_data = {
            "ability_score": AbilityScore.objects.first().id,
            "arcana": 4
        }

        response = client.post("/api/skills/create/", data=skills_data, format="json")

        self.assertEqual(response.status_code, 201)
        skills_entry = Skills.objects.first()
        self.assertNotEqual(4, skills_entry.arcana)

    def test_skills_post_ignores_extra_fields_in_request(self):
        """
        Test that any extra data in the request parameters is ignored except 'ability_score' field.

        :return: None
        """
        client = APIClient()
        skills_data = {
            "ability_score": AbilityScore.objects.first().id,
            "junk": 289871,
            "string": "Weeee"
        }

        response = client.post("/api/skills/create/", data=skills_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_skill_double_post(self):
        """
        Test to verify that a two posts cannot occur for the same ability score entry
        :return: None
        """

        client = APIClient()
        new_skill = {
            "ability_score": AbilityScore.objects.first().id
        }

        response = client.post("/api/skills/create/", data=new_skill, format="json")
        self.assertEqual(response.status_code, 201)
        # Ensures that the relationship is OneToOne
        response = client.post("/api/skills/create/", data=new_skill, format="json")
        self.assertEqual(response.status_code, 400)
