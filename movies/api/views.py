from movies.models import Movies ,Actors ,Genre
from .serializers import MovieSerializers
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated,])
def index(request):
    if request.method=='GET':
        movies = Movies.objects.all()
        serializer = MovieSerializers(movies,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated,])
def edit(request,pk):
    try:
        movie=Movies.objects.get(pk=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializers(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#params search
class moviesList(generics.ListAPIView):
    serializer_class = MovieSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Movies.objects.all()
        for x in self.request.GET :
            if(x=='name'):
            queryset = queryset.filter(name__icontains=self.request.query_params.get('name')) | queryset.filter(genres__name__iexact=self.request.query_params.get('name')) | queryset.filter(actors__name__icontains=self.request.query_params.get('name'))    
        return queryset


# genre=self.request.query_params.get('genre')
#         if genre is not None:
#             queryset = queryset.filter(genres__name__iexact =genre)

#   for x in self.request.GET :
#             if(x=='name'):
#                 queryset = queryset.filter(name__icontains=self.request.query_params.get('name'))
#             if(x=='rate'):
#                 queryset = queryset.filter(rate=self.request.query_params.get('rate'))
#             if(x=='actor'):
#                 queryset = queryset.filter(actors__in=self.request.query_params.get('actor'))    
