from rest_framework import serializers
from movies.models import Movies,Actors ,Genre,Writer


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model =Actors
        fields= '__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model =Genre
        fields= '__all__'

class WriteSerializers(serializers.ModelSerializer):
    class Meta:
        model =Writer
        fields= '__all__'

class MovieSerializers(serializers.ModelSerializer):
    actors = ActorSerializers(many=True,read_only=True)
    genres = GenreSerializers(many=True,read_only=True)
    writers = WriteSerializers(many=True,read_only=True)

    class Meta:
        model =Movies
        fields= '__all__'
