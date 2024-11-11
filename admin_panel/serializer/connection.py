from rest_framework import serializers
from other_app.models import Connection, Connection_Category, Connection_Value

class ConnectionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'phone', 'phone_two', 'address', 'location', 'email', 'map', 'created_time', 'updated_time']


class ConnectionCategorySerializer(serializers.ModelSerializer):

    class Meta: 
        model = Connection_Category
        fields = ['id', 'title']


class ConnectionValueSerializer(serializers.ModelSerializer):
    connection_title = serializers.SerializerMethodField()
    
    class Meta: 
        model = Connection_Value
        fields = ['id', 'connection_category','connection_title',  'value']
    

    def get_connection_title(self, obj):
        name = obj.connection_category.title
        return name
