from rest_framework import serializers
from Series.models import Series
from movies.models import Actors ,Genre

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model =Actors
        fields= ('name',)

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model =Genre
        fields= ('name',)

class SeriesSerializer(serializers.ModelSerializer):
    actors = ActorSerializers(many=True,read_only=True)
    genre = GenreSerializers(many=True,read_only=True)
    class Meta:
        model = Series
        fields = '__all__'
