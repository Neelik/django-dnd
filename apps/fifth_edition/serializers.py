from apps.fifth_edition import models
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Character model
    """

    class Meta:
        model = models.Character
        fields = "__all__"
