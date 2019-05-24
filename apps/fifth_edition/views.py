from .models import Character, AbilityScore, Skills, Spellcasting, Save
from .serializers import (CharacterSerializer, AbilityScoreSerializer, SkillsSerializer,
                          SpellcastingSerializer, SaveSerializer)
from .common import orm_ify_query_params
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny


class AbilityScoreViewGET(ListAPIView):
    """
    View to retrieve Ability Score objects

    """
    permission_classes = (AllowAny,)
    serializer_class = AbilityScoreSerializer

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of Ability Score objects to be returned by the API

        :return: QuerySet of Ability Score objects
        """

        query_params = orm_ify_query_params(self.request.query_params, "Ability Score")
        queryset = AbilityScore.objects.none()
        queryset = queryset | AbilityScore.objects.filter(**query_params)

        return queryset.order_by("id")


class CharacterViewGET(ListAPIView):
    """
    View to retrieve Character objects

    """
    permission_classes = (AllowAny,)
    serializer_class = CharacterSerializer

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of Character objects to be returned by the API

        :return: QuerySet of Character objects
        """

        query_params = orm_ify_query_params(self.request.query_params, "Character")
        queryset = Character.objects.none()
        queryset = queryset | Character.objects.filter(**query_params)

        return queryset.order_by("-level")


class CharacterViewPOST(CreateAPIView):
    """
    Class to create new Character entries

    """
    permission_classes = (AllowAny,)
    serializer_class = CharacterSerializer
    queryset = Character.objects.none()


class SaveViewGET(ListAPIView):
    """
    Class to retrieve Save objects
    """

    permission_classes = (AllowAny,)
    serializer_class = SaveSerializer

    def get_queryset(self):
        """
        Method to return the appropriate QuerySet of Save objects

        :return: QuerySet of Save objects
        """
        queryset = Save.objects.none()
        queryset = queryset | Save.objects.filter(ability_score=self.kwargs.get("id"))

        return queryset.order_by("id")


class SaveViewPOST(CreateAPIView):
    """
    Class to create new Save objects
    """
    permission_classes = (AllowAny,)
    serializer_class = SaveSerializer
    queryset = Save.objects.none()


class SkillsViewPOST(CreateAPIView):
    """
    Class to create new Skills entries
    """
    permission_classes = (AllowAny,)
    serializer_class = SkillsSerializer
    queryset = Skills.objects.none()


class SpellcastingViewGET(ListAPIView):
    """
    Class to retrieve Spellcasting entries
    """
    permission_classes = (AllowAny,)
    serializer_class = SpellcastingSerializer

    def get_serializer(self, *args, **kwargs):
        """
        Custom definition of get_serializer method that allows us to customize the fields dynamically based on
        keyword arguments passed in the request

        :param args: Pass through of args dictionary
        :param kwargs: Pass through of kwargs dictionary
        :return: Modified or unmodified Serializer with necessary fields values
        """

        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        if "field" in self.request.query_params:
            field = self.request.query_params["field"]
            if field == "attack":
                kwargs["fields"] = ("id", "spell_attack")
            elif field == "spell_save":
                kwargs["fields"] = ("id", "spell_save")

        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of Characters Skills to be returned by the API

        :return: Query Set of Skills objects
        """

        queryset = Spellcasting.objects.none()
        queryset = queryset | Spellcasting.objects.filter(ability_score=self.kwargs.get("id"))

        return queryset.order_by("id")


class SpellcastingViewPOST(CreateAPIView):
    """
    Class to create new Spellcasting entries
    """
    permission_classes = (AllowAny,)
    serializer_class = SpellcastingSerializer
    queryset = Spellcasting.objects.none()
