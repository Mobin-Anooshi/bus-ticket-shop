from rest_framework import serializers
from home.models import Travel




class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields=('origin','destination','time','price')
        