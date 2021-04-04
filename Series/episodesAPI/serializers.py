from rest_framework import serializers
from Series.models import Episodes

class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = '__all__'

