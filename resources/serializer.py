from rest_framework import serializers

# from admin_panel.serializer.resources import Base64FileField, ResourceAdminSerializer

from django.core.files.base import ContentFile
import six
import base64

from rest_framework.pagination import PageNumberPagination

from .models import Gallery, File, Audio, VirtualReality, Video, \
    Location, Resource, Category, PeriodFilter, FilterCategories, Filters, Province, Contents, Attributes

class ResourcePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page'
    max_page_size = 100


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # If the base64 string is in the "data:" URL scheme, strip it off
            if data.startswith('data:image'):
                # Find the comma in the base64 string
                comma_index = data.find(',')
                if comma_index != -1:
                    data = data[comma_index + 1:]

            # Decode the base64 string
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name
            file_name = self.get_file_name(decoded_file)
            data = ContentFile(decoded_file, name=file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_name(self, decoded_file):
        # Generate file name
        import uuid
        file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
        return '{}.png'.format(file_name)


class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'
    
    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon and request:
            return request.build_absolute_uri(obj.icon.url)
        return None

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class PeriodFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodFilter
        fields =  ('id', 'title')


class FilterCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCategories
        fields = ('id', 'title')


class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = ('id', 'title', 'filter_category')


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'image', 'image')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'title', 'audio')


class VirtualRealitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualReality
        fields = ('id', 'title', 'audio')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'file', 'link',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'latitude', 'longitude')


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('id', 'title', 'description')


class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ('id', 'title', 'description')


# class ResourceSerializer(serializers.ModelSerializer):
#     category_name = serializers.SerializerMethodField()
#     filter_category_title = serializers.SerializerMethodField()

#     attributes = AttributesSerializer(many=True, read_only=True)
#     contents = ContentsSerializer(many=True, read_only=True)
#     galleries = GallerySerializer(many=True, read_only=True)
#     files = FileSerializer(many=True, read_only=True)
#     audios = AudioSerializer(many=True, read_only=True)
#     virtual_realities = VirtualRealitySerializer(many=True, read_only=True)
#     videos = VideoSerializer(many=True, read_only=True)
#     locations = LocationSerializer(many=True, read_only=True)

#     class Meta:
#         model = Resource
#         fields = [
#             'id', 'category', 'filter_category', 'filters', 'period_filter', 'title',
#             'image', 'statehood', 'province', 'category_name',
#             'filter_category_title', 'attributes', 'contents', 'galleries',
#             'files', 'audios', 'virtual_realities', 'videos', 'locations'
#         ]

#     def get_category_name(self, obj):
#         return obj.category.title if obj.category else None

#     def get_filter_category_title(self, obj):
#         return obj.filter_category.title if obj.filter_category else None

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)

#         request = self.context.get('request')

#         def build_absolute_url(path):
#             if path and not path.startswith('http'):
#                 return self.context['request'].build_absolute_uri(path)
#             return path

#         # Absolyut URL'larni yaratish
#         if 'image' in representation:
#             representation['image'] = build_absolute_url(representation['image'])

#         for gallery in representation.get('galleries', []):
#             if 'image' in gallery:
#                 gallery['image'] = build_absolute_url(gallery['image'])

#         for file in representation.get('files', []):
#             if 'file' in file:
#                 file['file'] = build_absolute_url(file['file'])

#         return representation

# class ResourceSerializer(serializers.ModelSerializer):
#     category_name = serializers.SerializerMethodField()
#     filter_category_title = serializers.SerializerMethodField()

#     # Boolean maydonlar: fayllar va audio mavjudligini tekshirish uchun
#     has_image = serializers.SerializerMethodField()
#     has_audio = serializers.SerializerMethodField()
#     has_file = serializers.SerializerMethodField()
#     has_video = serializers.SerializerMethodField()

#     attributes = AttributesSerializer(many=True, read_only=True)
#     contents = ContentsSerializer(many=True, read_only=True)
#     galleries = GallerySerializer(many=True, read_only=True)
#     files = FileSerializer(many=True, read_only=True)
#     audios = AudioSerializer(many=True, read_only=True)
#     virtual_realities = VirtualRealitySerializer(many=True, read_only=True)
#     videos = VideoSerializer(many=True, read_only=True)
#     locations = LocationSerializer(many=True, read_only=True)

#     class Meta:
#         model = Resource
#         fields = [
#             'id', 'category', 'filter_category', 'filters', 'period_filter', 'title',
#             'image', 'statehood', 'province', 'category_name', 'filter_category_title',
#             'has_image', 'has_audio', 'has_file', 'has_video', 'attributes', 'contents',
#             'galleries', 'files', 'audios', 'virtual_realities', 'videos', 'locations'
#         ]

#     def get_category_name(self, obj):
#         return obj.category.title if obj.category else None

#     def get_filter_category_title(self, obj):
#         return obj.filter_category.title if obj.filter_category else None

#     # Image count() 0 dan katta bo'lsa True, aks holda False
#     def get_has_image(self, obj):
#         return obj.image is not None

#     # Audios count() 0 dan katta bo'lsa True, aks holda False
#     def get_has_audio(self, obj):
#         return obj.audios.count() > 0

#     # Files count() 0 dan katta bo'lsa True, aks holda False
#     def get_has_file(self, obj):
#         return obj.files.count() > 0

#     # Videos count() 0 dan katta bo'lsa True, aks holda False
#     def get_has_video(self, obj):
#         return obj.videos.count() > 0

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)

#         request = self.context.get('request')

#         def build_absolute_url(path):
#             if path and not path.startswith('http'):
#                 return request.build_absolute_uri(path)
#             return path

#         # Absolyut URL'larni yaratish faqat kerakli joylarda
#         if 'image' in representation and representation['image']:
#             representation['image'] = build_absolute_url(representation['image'])

#         return representation
class ResourceSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    filter_category_title = serializers.SerializerMethodField()

    attributes = AttributesSerializer(many=True, read_only=True)
    contents = ContentsSerializer(many=True, read_only=True)
    galleries = GallerySerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)
    audios = AudioSerializer(many=True, read_only=True)
    virtual_realities = VirtualRealitySerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = [
            'id', 'category', 'filter_category', 'filters', 'period_filter', 'title',
            'image', 'statehood', 'province', 'category_name', 'filter_category_title',
            'attributes', 'contents', 'galleries', 'files', 'audios', 'virtual_realities',
            'videos', 'locations'
        ]

    def get_category_name(self, obj):
        return obj.category.title if obj.category else None

    def get_filter_category_title(self, obj):
        return obj.filter_category.title if obj.filter_category else None

    def build_absolute_url(self, path):
        """
        Construct the absolute URL for the file path.
        """
        request = self.context.get('request')
        if request and path and not path.startswith('http'):
            return request.build_absolute_uri(path)
        return path

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Convert image and file fields to absolute URLs
        if instance.image:
            representation['image'] = self.build_absolute_url(instance.image.url)
        
        # Process related fields that may contain URLs
        for field in ['galleries', 'files', 'audios', 'videos', 'virtual_realities']:
            if field in representation:
                for item in representation[field]:
                    if 'file' in item and item['file']:
                        item['file'] = self.build_absolute_url(item['file'])
                    if 'image' in item and item['image']:
                        item['image'] = self.build_absolute_url(item['image'])
                    if 'audio' in item and item['audio']:
                        item['audio'] = self.build_absolute_url(item['audio'])
        
        return representation


class ResourceCatSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = ['id', 'title', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ResourceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class CategoryResourceSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'icon', 'image', 'resources']

    def get_resources(self, obj):
        request = self.context['request']
        resources = obj.resources.all()

        paginator = ResourcePagination()
        page = paginator.paginate_queryset(resources, request)
        if page is not None:
            return paginator.get_paginated_response(
                ResourceCatSerializer(page, many=True, context=self.context).data).data

        return ResourceCatSerializer(resources, many=True, context=self.context).data
    

class CategoryResourceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'icon', 'image']


# Behruz


class LocationSerializer(serializers.ModelSerializer):
    resource_title = serializers.CharField(source='resource.title')
    category_id = serializers.IntegerField(source='resource.category.id')
    resource_id = serializers.IntegerField(source='resource.id')

    class Meta:
        model = Location
        fields = ['resource_title', 'category_id', 'resource_id', 'latitude', 'longitude']


class FiltersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = ("id", "title",)


class FilterCategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCategories
        fields = ("id", "title",)
