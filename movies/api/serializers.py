from rest_framework import serializers
from movies.models import Movies,Actors ,Genre,Writer


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model =Actors
        fields= ('name',)

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model =Genre
        fields= ('name',)

class WriteSerializers(serializers.ModelSerializer):
    class Meta:
        model =Writer
        fields= ('name',)

class MovieSerializers(serializers.ModelSerializer):
    actors = ActorSerializers(many=True,read_only=True)
    genres = GenreSerializers(many=True,read_only=True)
    writers = WriteSerializers(many=True,read_only=True)

    class Meta:
        model =Movies
        fields= ('id','name','description','release_year','maturity_rating','duration','views','rate','director','trailer','video','poster','writers','genres' ,'actors')
