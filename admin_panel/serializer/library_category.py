from rest_framework import serializers
from other_app.models import Library_Category

class Library_CategoryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Category
        fields = ['id','title', 'image', 'created_time', 'updated_time']
