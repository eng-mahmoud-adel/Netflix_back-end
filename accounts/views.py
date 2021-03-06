from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets 
from .serializers import ProfileSerializer, PaymentSerializer 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

###### logout the current authenticated user
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete() 
        
        return Response(data={
            'success': True,
            'message': 'logged out successfully'
        }, status=status.HTTP_200_OK)

###### get all profiles for one account

@permission_classes([IsAuthenticated,])
@api_view(['get'])
def profiles(request):
    try:
        profile = Profile.objects.filter(user= request.user.id)
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={
            "success":False,
            "errors":str(e)
        },status=status.HTTP_404_NOT_FOUND)

###### get one profile for one account

@permission_classes([IsAuthenticated,])
@api_view(['get'])
def profile(request, id):
    try:
        profile = Profile.objects.get(id = id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)

    except Exception as e:
        return Response(data={
            "success":False,
            "errors":str(e)
        },status=status.HTTP_404_NOT_FOUND)


###### create profile for one account

@permission_classes([IsAuthenticated,])
@api_view(['post'])
def create_profile(request):
    request.data._mutable = True
    request.data.update({"user": request.user.id})
    print(request.data)
    # request.data._mutable = False
    serializer = ProfileSerializer(data=request.data)
    # request.data.update({"user": request.user.id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_404_NOT_FOUND)


###### update and delete profile for one account

@permission_classes([IsAuthenticated,])
@api_view(['PUT','DELETE'])
def update_delete_profile(request, id):
    profile = Profile.objects.get(id = id)
    if request.method == 'PUT':

        if not request.data._mutable:
            request.data._mutable = True
            request.data.update({"user": request.user.id})
            print(request.data)
            request.data._mutable = False

        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)

###### Social login by google
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    # callback_url = 'http://localhost:8000'
    # callback_url = 'http://localhost:8000/api/accounts/auth/google/login/callback/'



###### create payment record for new user

@permission_classes([IsAuthenticated,])
@api_view(['post'])
def create_payment(request):
    # request.data._mutable = True
    request.data.update({"user": request.user.id})
    print(request.data)
    # request.data._mutable = False
    serializer = PaymentSerializer(data=request.data)
    # request.data.update({"user": request.user.id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_404_NOT_FOUND)


# class IsManager(BasePermission):
#     # group = Group(name = "Manager")
#     # #group.save()                    # save this new group for this example
#     # user = User.objects.get(pk = 1) # assuming, there is one initial user 
#     # user.groups.add(group)          # user is now in the "Editor" group
#     def has_permission(self,request, view):
#         return request.user.has_perm("netflix.add_movie")