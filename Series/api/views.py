from rest_framework.response import Response
from Series.models import Series
from .serializers import SeriesSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated


class SeriesList(generics.ListAPIView):
    serializer_class = SeriesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Series.objects.all()
        for x in self.request.GET :
            if(x=='name'):
                queryset = queryset.filter(name__icontains=self.request.query_params.get('name')) | queryset.filter(genre__name__iexact=self.request.query_params.get('name')) | queryset.filter(actors__name__icontains=self.request.query_params.get('name'))    
      
        return queryset

#class CreateSeries(generics.CreateAPIView):
#    queryset = 	Series.objects.all()
#    serializer_class= SeriesSerializer


# class DeleteSeries(generics.DestroyAPIView):
#     queryset = 	Series.Objects.all()  
#     serializer_class= SeriesSerializer


@api_view(["GET",])
@permission_classes([IsAuthenticated,])
def index(request):
    series=Series.objects.all()
    serializer = SeriesSerializer(instance=series, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["POST",])
@permission_classes([IsAuthenticated,])
def create(request):
     serializer = SeriesSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(data={
 	    "success":True,
 	    "message": "Series has been added"
 	}, status=status.HTTP_200_OK)
     return Response(data={
 	    "success":False,
 	    "errors": serializer.errors
 	}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST","PUT"])
@permission_classes([IsAuthenticated,])
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


# @api_view(["DELETE"])
# def delete(request, pk):
#     serie=Series.objects.get(pk=pk)
#     serie.delete()
#     return Response(data={
#         "success":True,
#         "message":"Series Has Been Deleted"
#     },status=status.HTTP_204_NO_CONTENT)



class RetrieveSeries(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class DeleteSeries(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer