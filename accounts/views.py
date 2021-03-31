from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from django.contrib.auth.models import User, Group
from .serializers import UserSerializer
from rest_framework.decorators import api_view ,permission_classes
#from authentication.permissions import IsNotAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,authenticate




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



# class IsManager(BasePermission):
#     # group = Group(name = "Manager")
#     # #group.save()                    # save this new group for this example
#     # user = User.objects.get(pk = 1) # assuming, there is one initial user 
#     # user.groups.add(group)          # user is now in the "Editor" group
#     def has_permission(self,request, view):
#         return request.user.has_perm("netflix.add_movie")