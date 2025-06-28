from django.shortcuts import render
from django.http.response import  JsonResponse
from rest_framework.response import Response  # <-- Import Response from rest_framework 
from .models import Guest,Movie,Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer
from rest_framework import status,filters
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
def no_rest_no_model(request):
            guests = [
                {
                    'id': 1 ,
                    'Name':"atef",
                    'mobile':548945,
                },
                
                {
                    'id':2,
                    'Name':"zyad",
                    'mobile':548945,
                }   
            ]
            return JsonResponse (guests,safe=False)

def no_rest_with_model(request):
    data = Guest.objects.all()
    respons= {
        'guest':list(data.values('name','mobile'))
    }
    return JsonResponse(respons)

@api_view(['GET','POST'])
def FBV(request):
    if request.method=='GET':
        guests = Guest.objects.all()
        serializer= GuestSerializer(guests,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def FBV_PK(request,pk):
    try:
        guest = Guest.objects.get(pk= pk)
    except guest.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method=='GET':
        serializer= GuestSerializer(guest)
        return Response(serializer.data)
    
    #PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    elif request.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CBV(APIView):
    def get(self , request):
          guests = Guest.objects.all()
          serializer= GuestSerializer(guests,many=True)
          return Response(serializer.data)
    def post(self,request):
         serializer = GuestSerializer(data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class CBV_PK(APIView):
    def get_object(self,pk):
         try:
            return Guest.objects.get(pk=pk)
         except Guest.DoesNotExist: 
            raise Http404
    # GET: retrieve one object by pk
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    # PUT: update one object by pk
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: delete one object by pk
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin
,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

# Retrieve, update, or delete a single guest by pk
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
    
class GuestList(ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# Retrieve, update, or delete a guest by pk
class GuestDetail(RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    
    
    
    
    
    
    
    