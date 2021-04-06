# Serialize the Alias Model
from rest_framework import serializers
from .models import Aliases

class AliasesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aliases
        # using all keyword than using list
        fields = "__all__"