from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    # terms = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ["email","password","date_joined"]

    def save(self,**kwargs):
        user = User(
            # first_name= self.validated_data.get('first_name'),
            # last_name= self.validated_data.get('last_name'),
            email = self.validated_data.get('email'),
            # username = self.validated_data.get('username'),
            
        )
        
        user.set_password(self.validated_data.get('password'))
        user.save()
        print(user)
        Token.objects.get_or_create(user=user)
        print(Token.objects.get(user=user))

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        # fields= ('name',)