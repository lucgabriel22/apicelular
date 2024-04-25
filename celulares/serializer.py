from .models import CelularesBase, Avaliacao
from rest_framework import serializers

class CelularesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelularesBase
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'read_only': True}
        }
        
        model = Avaliacao
        fields = '__all__'