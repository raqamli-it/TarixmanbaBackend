from django.http import Http404
from other_app.models import Connection_Category
from admin_panel.serializer.connection import ConnectionCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class ConnectionFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Connection_Category
        fields = ['title']


# Create (Yaratish)
@api_view(['POST'])
def create_connection_category(request):
    serializer = ConnectionCategorySerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_connection_category(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    connections = Connection_Category.objects.all().order_by("id")
    connections_cat_filter = ConnectionFilter(request.GET, queryset=connections)
    result_page = paginator.paginate_queryset(connections_cat_filter.qs, request)
    serializer = ConnectionCategorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def connection_category_detail(request, pk):
    try:
        connection = Connection_Category.objects.get(pk=pk)
    except Connection_Category.DoesNotExist:
        raise Http404

    serializer = ConnectionCategorySerializer(connection)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_connection_category(request, pk):
    try:
        connection = Connection_Category.objects.get(pk=pk)
    except Connection_Category.DoesNotExist:
        return Response({'error': 'Connection not found'}, status=404)

    serializer = ConnectionCategorySerializer(connection, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_connection_category(request, pk):
    try:
        connection = Connection_Category.objects.get(pk=pk)
    except Connection_Category.DoesNotExist:
        return Response({'error': 'Connection not found'}, status=404)

    connection.delete()
    return Response(status=204)

