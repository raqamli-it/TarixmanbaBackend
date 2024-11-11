from django.http import Http404
from other_app.models import Library_Category
from admin_panel.serializer.library_category import Library_CategoryAdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class LibraryCatFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Library_Category
        fields = ['title']



# Create (Yaratish)
@api_view(['POST'])
def create_library_category(request):
    serializer = Library_CategoryAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_library_categories(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    categories = Library_Category.objects.all().order_by("id")
    library_cat__filter = LibraryCatFilter(request.GET, queryset=categories)
    result_page = paginator.paginate_queryset(library_cat__filter.qs, request)
    serializer = Library_CategoryAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def library_category_detail(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        raise Http404

    serializer = Library_CategoryAdminSerializer(category)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_library_category(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        return Response({'error': 'Library Category not found'}, status=404)

    serializer = Library_CategoryAdminSerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_library_category(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        return Response({'error': 'Library Category not found'}, status=404)

    category.delete()
    return Response(status=204)
