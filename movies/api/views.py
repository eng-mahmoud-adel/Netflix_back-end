from movies.models import Movies
from .serializers import MovieSerializers
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


@api_view(["GET","POST"])
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
def edit(request,pk):
    try:
        movie=Movies.objects.get(pk=pk)
        print(movie)
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

class moviesList(generics.ListAPIView):
    serializer_class = MovieSerializers
    def get_queryset(self):
        queryset = Movies.objects.all()
        name=self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset