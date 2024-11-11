from rest_framework import serializers
from other_app.models import Library


class LibraryAdminSerializer(serializers.ModelSerializer):
    cat_library = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = ['id', 'title', 'category', 'author', 'type', 'year', 'country', 'language', 'image', 'file',
                  'created_time', 'updated_time', 'cat_library']

    def get_cat_library(self, obj):
        cat = obj.category
        if cat:
            return cat.title


