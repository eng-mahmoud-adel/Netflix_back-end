from rest_framework.response import Response
from Series.models import Episodes
from .serializers import EpisodesSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET",])
@permission_classes([IsAuthenticated,])
def index(request):
    episode = Episodes.objects.all()
    serializer = EpisodesSerializer(instance=episode, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(["POST",])
@permission_classes([IsAuthenticated,])
def create(request):
    serializer = EpisodesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Episodes Has Been Created Successfully"
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "message":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT",])
@permission_classes([IsAuthenticated,])
def update(request,pk):
    episode = Episodes.objects.get(pk=pk)
    serializer = EpisodesSerializer(data=request.data,instance=episode)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "Success:": True,
            "message": "Episode Has Been Updated"
        },status=status.HTTP_200_OK)
    return Response(data={
        "Success:": False,
        "message": serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)

@api_view(["Delete",])
@permission_classes([IsAuthenticated,])
def delete(request,pk):
    episode = Episodes.objects.get(pk=pk)
    episode.delete()
    return Response(data={
        "success":True,
        "message":"Episode Has Been Deleted"
    },status=status.HTTP_204_NO_CONTENT)

class RetrieveEpisode(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializer

class DeleteEpisode(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializer


class episodesList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EpisodesSerializer
    def get_queryset(self):
        queryset = Episodes.objects.all()
        for x in self.request.GET :
            if(x=='sid'):
                queryset = queryset.filter(series_id__exact=self.request.query_params.get('sid'))  

        return queryset