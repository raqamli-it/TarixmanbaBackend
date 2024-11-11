from rest_framework import serializers
from other_app.models import About

class AboutAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'created_time', 'updated_time')
        