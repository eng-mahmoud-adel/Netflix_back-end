from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,viewsets 
#from django.contrib.auth.models import User, Group
from .serializers import UserSerializer,ProfileSerializer
from rest_framework.decorators import api_view ,permission_classes
#from authentication.permissions import IsNotAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,authenticate
from .models import Profile



class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete() 
        
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    print(request.data.get('username'))
    if serializer.is_valid():
        try:
            serializer.save()
            # username= serializer.data.get("username")
            # password= serializer.data.get("password")
            # user = authenticate(username=username,password=password)
            # login(request,user)
        except Exception as e:
            return Response(data={
                    "success":False,
                    "errors":str(e)
            },status=status.HTTP_400_BAD_REQUEST)
        return Response(data={
            "success":True,
            "message":"User has been created successfully",
            # "token":Token.objects.get(user=request.data.get('username'))
        },status=status.HTTP_201_CREATED)
    return Response(data={
            "success":False,
            "passsword":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)



###### get all profiles for one account

@api_view(['get'])
def api_profiles(request,user):
    try:
        profile = Profile.objects.filter(user_set= user)
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={
            "success":False,
            "errors":str(e)
        },status=status.HTTP_404_NOT_FOUND)

###### get one profile for one account

@api_view(['get'])
def api_profile(request,id):
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

@api_view(['post'])
def create_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_404_NOT_FOUND)


###### update and delete profile for one account

@api_view(['PUT','DELETE'])
def up_del_profile(request,id):
    profile = Profile.objects.get(id = id)
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# class IsManager(BasePermission):
#     # group = Group(name = "Manager")
#     # #group.save()                    # save this new group for this example
#     # user = User.objects.get(pk = 1) # assuming, there is one initial user 
#     # user.groups.add(group)          # user is now in the "Editor" group
#     def has_permission(self,request, view):
#         return request.user.has_perm("netflix.add_movie")