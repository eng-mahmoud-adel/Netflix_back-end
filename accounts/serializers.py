from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile, Payment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     # terms = serializers.BooleanField(default=False)
#     profile = ProfileSerializer(many=True)

#     class Meta:
#         model = User
#         fields = ["email","password","date_joined"]

#     def save(self,**kwargs):
#         user = User(
#             # first_name= self.validated_data.get('first_name'),
#             # last_name= self.validated_data.get('last_name'),
#             email = self.validated_data.get('email'),
#             # username = self.validated_data.get('username'),
            
#         )
        
#         user.set_password(self.validated_data.get('password'))
#         user.save()
#         print(user)
#         Token.objects.get_or_create(user=user)
#         print(Token.objects.get(user=user))