from rest_framework import serializers
from other_app.models import News

class NewsAdminSerializer(serializers.ModelSerializer):

    file_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id','title', 'content', 'file_url',  'created_time', 'updated_time']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None