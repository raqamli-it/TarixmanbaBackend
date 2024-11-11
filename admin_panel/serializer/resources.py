from itertools import zip_longest
from django.db import transaction
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.request import Request
import json
from Config import settings
from resources.models import Category, PeriodFilter, Filters, Resource, Province,  Attributes, Contents, FilterCategories
import uuid
import base64
import six
import re
import logging

logger = logging.getLogger(__name__)

class Base64FileField(serializers.FileField):
    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_file')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = f"{file_name}.{file_extension}"

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64FileField, self).to_internal_value(data)
    
    def get_file_extension(self, file_name, decoded_file):
        try:
            import magic
            file_mime_type = magic.from_buffer(decoded_file, mime=True)
            return file_mime_type.split('/')[-1]
        except ImportError:
            return 'jpg'

# class Base64FileField(serializers.FileField):
#     def to_internal_value(self, data):
#         # If data is a base64 string, handle it here.
#         if isinstance(data, str) and data.startswith('data:'):
#             # Get the file format and base64 string
#             format, imgstr = data.split(';base64,') 

#             # Handle incorrect padding
#             imgstr += '=' * (4 - len(imgstr) % 4)
            
#             try:
#                 # Decode the base64 string
#                 decoded_file = base64.b64decode(imgstr)
#             except (TypeError, binascii.Error):
#                 raise serializers.ValidationError("Invalid image format")

#             # Generate file name
#             file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
#             # Get the file extension from the format part
#             file_extension = format.split('/')[-1]
            
#             complete_file_name = f"{file_name}.{file_extension}"
            
#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64FileField, self).to_internal_value(data)



class FiltersAdminSerializer(serializers.ModelSerializer):
    filter_categories_name = serializers.SerializerMethodField()
    filter_cat_id = serializers.SerializerMethodField()
    cat_id = serializers.SerializerMethodField()
    cat_title = serializers.SerializerMethodField()

    class Meta:
        model = Filters
        fields = ('id', 'title', 'filter_category', 'created_time',
                  'updated_time', 'filter_cat_id', 'filter_categories_name', 'cat_id',
                  'cat_title',)

    def get_filter_categories_name(self, obj):
        filter_cat = obj.filter_category
        if filter_cat:
            return filter_cat.title

    def get_filter_cat_id(self, obj):
        filter_cat = obj.filter_category
        if filter_cat:
            return filter_cat.id

    def get_cat_id(self, obj):
        cat_id = obj.filter_category
        if cat_id:
            cat = cat_id.category
            if cat:
                return cat.id

    def get_cat_title(self, obj):
        cat_name = obj.filter_category
        if cat_name:
            cat = cat_name.category
            if cat:
                return cat.title


class FilterCategoriesAdminSerializer(serializers.ModelSerializer):
    filters_category = FiltersAdminSerializer(many=True, read_only=True)
    cat_title = serializers.SerializerMethodField()
    cat_id = serializers.SerializerMethodField()

    class Meta:
        model = FilterCategories
        fields = ('id', 'title', 'category', 'created_time', 'updated_time', 'filters_category', 'cat_title', 'cat_id')
        extra_kwargs = {
            'filters_category': {'read_only': True, 'required': False},
        }

    def get_filters_category(self, obj):
        return obj.filters_category.all()

    def get_cat_title(self, obj):
        title = obj.category
        if title:
            return title.title

    def get_cat_id(self, obj):
        cat = obj.category
        if cat:
            return cat.id


class CategoryAdminSerializer(serializers.ModelSerializer):
    categories = FilterCategoriesAdminSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'icon','image' ,'order', 'interactive', 'created_time', 'updated_time', 'categories',)
        extra_kwargs = {
            'categories': {'read_only': True, 'required': False},
        }



    def get_categories(self, obj):
        return obj.categories.all()



class PeriodFilterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodFilter
        fields = ('id', 'title', 'created_time', 'updated_time')


class ProvinceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'title','latitude', 'longitude', 'created_time', 'updated_time')


# class InteriveAdminSerializer(serializers.ModelSerializer):
#     file = serializers.FileField(max_length=None, use_url=True, allow_null=True)
#     link = serializers.URLField(allow_null=True)
#     latitude = serializers.CharField(max_length=500, allow_null=True)
#     longitude = serializers.CharField(max_length=500, allow_null=True)
#     status_display = serializers.CharField(source='get_status_display', read_only=True)

#     class Meta:
#         model = Interive
#         fields = ['resource_interive', 'status', 'status_display', 'title', 'file', 'link', 'latitude', 'longitude',
#                   'created_time', 'updated_time']


class AttributesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['resource_attribute', 'attributes_title', 'attributes_description', 'created_time', 'updated_time']


class ContentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['resource_content', 'contents_title', 'contents_description', 'created_time', 'updated_time']


class ResourceAdminSerializer(serializers.ModelSerializer):
    # interive = InteriveAdminSerializer(many=True, read_only=True)
    attributes = AttributesAdminSerializer(many=True, read_only=True)
    contents = ContentsAdminSerializer(many=True, read_only=True)
    interive_list = serializers.SerializerMethodField(required=False, read_only=True)
    attributes_list = serializers.SerializerMethodField(required=False, read_only=True)
    contents_list = serializers.SerializerMethodField(required=False, read_only=True)
    cat_name = serializers.SerializerMethodField(required=False, read_only=True)
    filter_category_name = serializers.SerializerMethodField(required=False, read_only=True)
    filters_name = serializers.SerializerMethodField(required=False, read_only=True)
    period_filter_name = serializers.SerializerMethodField(required=False, read_only=True)
    image = Base64FileField(max_length=None, use_url=True)
    province_name = serializers.SerializerMethodField(required=False, read_only=True)
    contents_title_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )
    contents_description_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )
    attributes_title_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )
    attributes_description_list = serializers.ListField(
        child=serializers.CharField(max_length=None, required=False),
        write_only=True,
        required=False
    )

    interive_data_list = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField(max_length=None, required=False)),
        write_only=True,
        required=False
    )

    filter_list = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    # 'filters',
    class Meta:
        model = Resource
        fields = (
            'id', 'category', 'filter_category', 'period_filter', 'title', 'image', 'content',
            'province_name', 'statehood',
            'province', 'interive', 'interive_data_list',
            'attributes_title_list', 'attributes_description_list', 'attributes',
            'contents_title_list', 'contents_description_list', 'contents',
            'interive_list', 'attributes_list', 'contents_list',
            'cat_name', 'filter_category_name', 'filters_name', 'period_filter_name', 'filter_list',
            'created_time', 'updated_time'
        )

    def get_interive_list(self, obj):
        return InteriveAdminSerializer(obj.resource_interive.all(), many=True).data

    def get_attributes_list(self, obj):
        return AttributesAdminSerializer(obj.resource_attribute.all(), many=True).data

    def get_contents_list(self, obj):
        return ContentsAdminSerializer(obj.resource_content.all(), many=True).data

    def get_cat_name(self, obj):
        cat = obj.category
        if cat:
            return cat.title

    def get_filter_category_name(self, obj):
        title = obj.filter_category
        if title:
            return title.title

    def get_filters_name(self, obj):
        filters = obj.filters.all()  # Get all filter objects
        if filters:
            return [filter.id for filter in filters]  # Return a list of titles
        return []  # Return an empty list if no filters are found

    def get_period_filter_name(self, obj):
        period = obj.period_filter
        if period:
            return period.title

    def get_province_name(self, obj):
        province = obj.province
        if province:
            return province.title



    @staticmethod
    def create_contents(resource, title_list, description_list):
        if title_list or description_list:
            for title, description in zip_longest(title_list or [''], description_list or [''], fillvalue=''):
                Contents.objects.create(resource_content=resource, contents_title=title,
                                        contents_description=description)
        else:
            Contents.objects.create(resource_content=resource, contents_title='', contents_description='')

    @staticmethod
    def create_attributes(resource, title_list, description_list):
        if title_list or description_list:
            for title, description in zip_longest(title_list or [''], description_list or [''], fillvalue=''):
                Attributes.objects.create(resource_attribute=resource, attributes_title=title,
                                          attributes_description=description)
        else:
            Attributes.objects.create(resource_attribute=resource, attributes_title='', attributes_description='')

    @transaction.atomic
    def create(self, validated_data):
        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])
        attributes_title_list = validated_data.pop('attributes_title_list', [])
        attributes_description_list = validated_data.pop('attributes_description_list', [])
        interive_data_list = validated_data.pop('interive_data_list', [], None)
        filter_list = validated_data.pop('filter_list', [])

        resource = Resource.objects.create(**validated_data)

        self.create_contents(resource, contents_title_list, contents_description_list)
        self.create_attributes(resource, attributes_title_list, attributes_description_list)
        for interive_data in interive_data_list:
            print("intrative", interive_data)
            Interive.objects.create(resource_interive=resource, **interive_data)

        resource.filters.set(filter_list)

        return resource

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.filter_category = validated_data.get('filter_category', instance)
        instance.filter_category = validated_data.get('filter_category', instance.filter_category)

        instance.period_filter = validated_data.get('period_filter', instance.period_filter)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.content = validated_data.get('content', instance.content)
        instance.statehood = validated_data.get('statehood', instance.statehood)
        instance.province = validated_data.get('province', instance.province)
        instance.save()

        contents_title_list = validated_data.pop('contents_title_list', [])
        contents_description_list = validated_data.pop('contents_description_list', [])
        attributes_title_list = validated_data.pop('attributes_title_list', [])
        attributes_description_list = validated_data.pop('attributes_description_list', [])
        interive_data_list = validated_data.pop('interive_data_list', [], None)
        filter_list = validated_data.pop('filter_list', [])

        instance.resource_content.all().delete()
        instance.resource_attribute.all().delete()
        instance.resource_interive.all().delete()

        self.create_contents(instance, contents_title_list, contents_description_list)
        self.create_attributes(instance, attributes_title_list, attributes_description_list)
        self.create_interive(instance, interive_data_list)

        instance.filters.set(filter_list)

        return instance
