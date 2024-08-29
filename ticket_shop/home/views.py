from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serailizers import TravelSerializer
from home.models import Travel

# Create your views here.



class HomeView(APIView):
    def get(self,request):
        travels = Travel.objects.filter(valid=True)
        ser_data = TravelSerializer(instance=travels,many=True)
        return Response(data=ser_data.data)
    
    