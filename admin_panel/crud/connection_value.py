from django.http import Http404
from other_app.models import Connection_Value
from admin_panel.serializer.connection import ConnectionValueSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class ConnectionValFilter(django_filters.FilterSet):
    value = django_filters.CharFilter(field_name='value', lookup_expr='icontains')

    class Meta:
        model = Connection_Value
        fields = ['value']


# Create (Yaratish)
@api_view(['POST'])
def create_connection_value(request):
    serializer = ConnectionValueSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_connection_value(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    connections = Connection_Value.objects.all().order_by("id")
    connections_val_filter = ConnectionValFilter(request.GET, queryset=connections)
    result_page = paginator.paginate_queryset(connections_val_filter.qs, request)
    serializer = ConnectionValueSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def connection_value_detail(request, pk):
    try:
        connection = Connection_Value.objects.get(pk=pk)
    except Connection_Value.DoesNotExist:
        raise Http404

    serializer = ConnectionValueSerializer(connection)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_connection_value(request, pk):
    try:
        connection = Connection_Value.objects.get(pk=pk)
    except Connection_Value.DoesNotExist:
        return Response({'error': 'Connection not found'}, status=404)

    serializer = ConnectionValueSerializer(connection, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_connection_value(request, pk):
    try:
        connection = Connection_Value.objects.get(pk=pk)
    except Connection_Value.DoesNotExist:
        return Response({'error': 'Connection not found'}, status=404)

    connection.delete()
    return Response(status=204)

