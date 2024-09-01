from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serailizers import TravelSerializer,CreateTravelSerializers,BuyTicketSerializer
from home.models import Travel
from permissions import IsDriverOnly
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.



class HomeView(APIView):
    permission_classes=[AllowAny,]
    def get(self,request):
        travels = Travel.objects.filter(valid=True)
        ser_data = TravelSerializer(instance=travels,many=True)
        return Response(data=ser_data.data)
    

class CreateTravel(APIView):
    permission_classes = [IsDriverOnly,] # Test mode
    def post(self,request):
        ser_data = CreateTravelSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data,request)
            return Response(data=ser_data.data)
        return Response(data=ser_data.errors)


class UserBuyTicket(APIView):
    permission_classes = [IsAuthenticated,] 
    def post(self,request):
        extra_data ={
            'user':request.user.id
        }
        ser_data = BuyTicketSerializer(data=request.POST,context=extra_data)
        if ser_data.is_valid() :
            ser_data.create(ser_data.validated_data,request)
            return Response(data=ser_data.data)
        return Response(ser_data.errors)
    