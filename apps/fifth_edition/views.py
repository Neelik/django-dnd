from .models import Character, NPC, AbilityScore, Skills, Spellcasting, Spell, Save, PhysicalAttack, CombatInfo, Background, Currency, Equipment, PhysicalDefense
from .serializers import (CharacterSerializer, NPCSerializer, AbilityScoreSerializer, SkillsSerializer,
                          SpellcastingSerializer, SpellSerializer, SaveSerializer, PhysicalAttackSerializer, EquipmentSerializer,
                          CombatInfoSerializer, BackgroundSerializer, CurrencySerializer, PhysicalDefenseSerializer)
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

class AbilityScoreViewPOST(CreateAPIView):
    """
    Class to create new ability score entries

    """
    permission_classes = (AllowAny,)
    serializer_class = AbilityScoreSerializer
    queryset = AbilityScore.objects.none()


class AbilityScoreViewPUT(RetrieveUpdateDestroyAPIView):
    """
    Method to PUT and DELETE Ability Scores

    :return: VOID
    """
    lookup_field = 'id'
    serializer_class = AbilityScoreSerializer
    queryset = AbilityScore.objects.all()


class EquipmentViewGET(ListAPIView):
	"""
	View to retrieve equipment objects
	"""
	lookup_field = 'id'
	serializer_class = EquipmentSerializer
	queryset = Equipment.objects.all()

class EquipmentViewPOST(CreateAPIView):
    """
    View to create new equipment objects
    """
    permission_classes = (AllowAny,)
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.none()

class EquipmentViewPUT(RetrieveUpdateDestroyAPIView):
    """
    View to PUT and DELETE an equipment object by id

	:return: None
    """
    lookup_field = 'id'
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class BackgroundViewGET(ListAPIView):
    """
    View to retrieve Background objects

    """
    permission_classes = (AllowAny,)
    serializer_class = BackgroundSerializer

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of Background objects to be returned by the API

        :return: QuerySet of Background objects
        """

        query_params = orm_ify_query_params(self.request.query_params, "Background")
        queryset = Background.objects.none()
        queryset = queryset | Background.objects.filter(**query_params)

        return queryset.order_by("id")


class BackgroundViewPOST(CreateAPIView):
    """
    Class to create new Background entries

    """
    permission_classes = (AllowAny,)
    serializer_class = BackgroundSerializer
    queryset = Background.objects.none()


class BackgroundViewPUT(RetrieveUpdateDestroyAPIView):
    """
    Method to PUT and DELETE a Background

    :return: None
    """

    lookup_field = 'id'
    serializer_class = BackgroundSerializer
    queryset = Background.objects.all()


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


class CharacterViewPUT(RetrieveUpdateDestroyAPIView):
    """
    Method to PUT and DELETE a character

    :return: VOID
    """

    lookup_field = 'id'
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CurrencyViewGET(ListAPIView):
	"""
	View to retrieve Currency objects
	"""
	lookup_field = 'id'
	serializer_class = CurrencySerializer
	queryset = Currency.objects.all()

class CurrencyViewPOST(CreateAPIView):
    """
    View to create new Currency objects
    """
    permission_classes = (AllowAny,)
    serializer_class = CurrencySerializer
    queryset = Currency.objects.none()

class CurrencyViewPUT(RetrieveUpdateDestroyAPIView):
    """
    View to PUT and DELETE an Currency object by id

	:return: None
    """
    lookup_field = 'id'
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class NPCViewGET(ListAPIView):
    """
    View to retrieve NPC objects

    """
    permission_classes = (AllowAny,)
    serializer_class = NPCSerializer

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of NPC objects to be returned by the API

        :return: QuerySet of NPC objects
        """

        query_params = orm_ify_query_params(self.request.query_params, "NPC")
        queryset = NPC.objects.none()
        queryset = queryset | NPC.objects.filter(**query_params)

        return queryset.order_by("-level")


class NPCViewPOST(CreateAPIView):
    """
    Class to create new NPC entries

    """
    permission_classes = (AllowAny,)
    serializer_class = NPCSerializer
    queryset = NPC.objects.none()


class NPCViewPUT(RetrieveUpdateDestroyAPIView):
    """
    Method to PUT and DELETE a NPC

    :return: VOID
    """

    lookup_field = 'id'
    serializer_class = NPCSerializer
    queryset = NPC.objects.all()


class CombatInfoViewGET(ListAPIView):
    """
    View to retrieve Combat Info objects

    """
    permission_classes = (AllowAny,)
    serializer_class = CombatInfoSerializer

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of Combat Info to be returned by the API

        :return: Query Set of Combat Info objects
        """

        query_params = orm_ify_query_params(self.request.query_params, "Combat Info")
        queryset = CombatInfo.objects.none()
        queryset = queryset | CombatInfo.objects.filter(**query_params)

        return queryset.order_by("id")


class CombatInfoViewPOST(CreateAPIView):
    """
    Class to create new Combat Info entries
    """
    permission_classes = (AllowAny,)
    serializer_class = CombatInfoSerializer
    queryset = CombatInfo.objects.none()


class CombatInfoViewPUT(RetrieveUpdateDestroyAPIView):
    """
    Method to PUT and DELETE a Combat Info

    :return: None
    """

    lookup_field = 'id'
    serializer_class = CombatInfoSerializer
    queryset = CombatInfo.objects.all()


class PhysicalDefenseViewGET(ListAPIView):
	"""
	Class to retrieve PhysicalDefense entries
	"""
	lookup_field = 'id'
	serializer_class = PhysicalDefenseSerializer
	queryset = PhysicalDefense.objects.all()

class PhysicalDefenseViewPOST(CreateAPIView):
	"""
	View to create new PhysicalDefense objects
	"""
	permission_classes = (AllowAny,)
	serializer_class = PhysicalDefenseSerializer
	queryset = PhysicalDefense.objects.none()

class PhysicalDefenseViewPUT(RetrieveUpdateDestroyAPIView):
    """
    View to PUT and DELETE an PhysicalDefense object by id

	:return: None
    """
    lookup_field = 'id'
    serializer_class = PhysicalDefenseSerializer
    queryset = PhysicalDefense.objects.all()


class PhysicalAttackViewGET(ListAPIView):
    """
    Class to retrieve Physical Attack entries
    """
    permission_classes = (AllowAny,)
    serializer_class = PhysicalAttackSerializer

    def get_queryset(self):
        """
        Method to return the appropriate QuerySet of Physical Attack entries
        :return: QuerySet of Physical Attack entries
        """
        query_params = orm_ify_query_params(self.request.query_params, "Physical Attack")
        queryset = PhysicalAttack.objects.none()
        queryset = queryset | PhysicalAttack.objects.filter(**query_params)

        return queryset.order_by("id")


class PhysicalAttackViewPOST(CreateAPIView):
    """
    Class to create new Physical Attack entries
    """
    permission_classes = (AllowAny,)
    serializer_class = PhysicalAttackSerializer
    queryset = PhysicalAttack.objects.none()


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


class SkillsViewGET(ListAPIView):
    """
    Class to retrieve new Skills entries

    """
    permission_classes = (AllowAny,)
    serializer_class = SkillsSerializer

    def get_queryset(self):
        """
        Method to retrieve the appropriate queryset of Characters Skills to be returned by the API

        :return: Query Set of Skills objects
        """

        queryset = Skills.objects.none()
        queryset = queryset | Skills.objects.filter(ability_score=self.kwargs.get("id"))

        return queryset.order_by("id")


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
            elif field == "spell_slots":
                kwargs["fields"] = ("id", "spell_slots")

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


class SpellViewGET(ListAPIView):
	"""
	View to retrieve equipment objects
	"""
	lookup_field = 'id'
	serializer_class = SpellSerializer
	queryset = Spell.objects.all()

class SpellViewPOST(CreateAPIView):
    """
    View to create new spell
    """
    permission_classes = (AllowAny,)
    serializer_class = SpellSerializer
    queryset = Spell.objects.none()

class SpellViewPUT(RetrieveUpdateDestroyAPIView):
    """
    View to PUT and DELETE an spell by id

	:return: None
    """
    lookup_field = 'id'
    serializer_class = SpellSerializer
    queryset = Spell.objects.all()

