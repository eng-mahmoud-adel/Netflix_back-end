from rest_framework import Response
from Series.models import Series
from .serializers import SeriesSerializer
from rest_framework import status
from rest_framework.decorators import api_views
from rest_framework import generics



class SeriesList(generic.ListAPIView):
    queryset = 	Series.Objects.all()    
    def get_queryset(self):
        queryset = Series.objects.all()
        name=self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class CreateSeries(generic.CreateAPIView):
    queryset = 	Series.Objects.all()  
    serializer_class= SeriesSerializer


# class DeleteSeries(generic.DestroyAPIView):
#     queryset = 	Series.Objects.all()  
#     serializer_class= SeriesSerializer


@api_view(["GET,"])
def index(request):
    serie=Series.object.all()  
    serializer = SeriesSerializer(instance=serie, many=True) 
    return Response(data=serializer.data, status=status.HTTP_200_OK)	

# @api_view(["POST,"])
# def create(request):
#     serializer = SeriesSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(data={
# 	    "success":True
# 	    "message": "Series has been added"
# 	}, status=status.HTTP_200_OK)
#     return Response(data={
# 	    "success":False
# 	    "errors": serializer.errors
# 	}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST","PUT"])
def update(request, id):
    serie=Series.objects.get(pk=id)
    serializer= SeriesSerializer(data=request.data, instance=serie)
    if serializer.is_valid():
        serializer.save()
        return Response(data=
        {
            "Success:": True,
            "message": "Series has been updated"
        },
        status=status.HTTP_200_OK)

    return Response(data=
        {
            "Success:": False,
            "message": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete(request, id):
    serie=Series.objects.get(pk=id)
    serie.delete()
    return Response(data=
        {
            "Success:": True,
            "message": "Series has been deleted"
        },
        status=status.HTTP_204_NO_CONTENT)