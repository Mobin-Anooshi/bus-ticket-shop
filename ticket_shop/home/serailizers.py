from rest_framework import serializers
from home.models import Travel
import math
from home.destination import main




class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields=('car','origin','destination','date','time','price')
        

        

class CreateTravelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Travel
        fields = ('car','driver','origin','destination','time','date')
    
    def create(self, validated_data):
        return Travel.objects.create(**validated_data)
    
    def validate(self,data):
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
        
            