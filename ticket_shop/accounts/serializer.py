from rest_framework import serializers
from accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('email','full_name','password','password2')
        extra_kwargs ={
            'password':{'write_only':True}
        }
        
        
    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(email=validated_data['email'],full_name=validated_data['full_name'],password=validated_data['password'])
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must match')
        return data
    
            