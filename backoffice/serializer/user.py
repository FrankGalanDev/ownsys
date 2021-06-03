from django.contrib.auth.models import User
#from backoffice.models import User
#from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    
def serialize(user):
    return{
	    'id': user.id,
	    'username': user.username,
	    'email': user.email,
        

        
        
}

#class GroupSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Group
        #fields = ['url', 'name']