from rest_framework import serializers
from Series.models import Episodes

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = '__all__'

