from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        # Is not necessary to know the data inside of the token, the only function is to be secret
        user.set_token(validated_data['email']) 
        user.save()
        return user

    def update(self,instance,validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))
        # Is not necessary to know the data inside of the token, the only function is to be secret
        instance.set_token(validated_data.get('token', instance.token)) 
        instance.save()
        return instance
        
    