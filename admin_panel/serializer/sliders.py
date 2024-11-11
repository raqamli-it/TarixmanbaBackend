from rest_framework import serializers
from other_app.models import Sliders

class SlidersAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = ['id','title', 'file', 'link', 'created_time', 'updated_time']