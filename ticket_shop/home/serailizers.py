from rest_framework import serializers
from home.models import Travel,Ticket
import math
from accounts.models import User
from django.shortcuts import get_object_or_404





class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields=('car','origin','destination','date','time','price')
        

        

class CreateTravelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Travel
        fields = ('car','driver','origin','destination','time','date')
    
    def create(self, validated_data,request):
        print(request)
        return Travel.objects.create(**validated_data)
    
    def validate(self,data,request):
        print(request)
        car= data.get('car')
        time = data.get('time').hour
        date = data.get('date')
        
        travels = Travel.objects.filter(car=car,date=date)
        if not travels.exists():
            return data
        
        in_travel = [travel for travel in travels if travel.time.hour<=time<=(travel.time.hour+math.ceil(travel.destance/80)+1)]
        if in_travel :
            raise serializers.ValidationError('bus in travel')
        return data
        

class BuyTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('travel',)
    def create(self, validated_data,request):
        user = User.objects.get(pk=request.user.id)
        return Ticket.objects.create(user = user , travel=validated_data['travel'],paid=True)
    
    def validate(self, data):
        user = self.context.get('user')
        user=get_object_or_404(User , pk=user)
        travel = get_object_or_404(Travel ,pk=data.get('travel').id)
        if user.wallet>= travel.price :
            user.wallet -=travel.price
            user.save()
            return data
        else :
            raise serializers.ValidationError('you dont have any mony')
        