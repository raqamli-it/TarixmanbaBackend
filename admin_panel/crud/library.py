from django.http import Http404
from other_app.models import Library
from admin_panel.serializer.library import LibraryAdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class LibraryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Library
        fields = ['title']



# Create (Yaratish)
@api_view(['POST'])
def create_library(request):
    serializer = LibraryAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_libraries(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    libraries = Library.objects.all().order_by("id")
    library_filter = LibraryFilter(request.GET, queryset=libraries)
    result_page = paginator.paginate_queryset(library_filter.qs, request)
    serializer = LibraryAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def library_detail(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        raise Http404

    serializer = LibraryAdminSerializer(library)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        return Response({'error': 'Library not found'}, status=404)

    serializer = LibraryAdminSerializer(library, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        return Response({'error': 'Library not found'}, status=404)

    library.delete()
    return Response(status=204)
