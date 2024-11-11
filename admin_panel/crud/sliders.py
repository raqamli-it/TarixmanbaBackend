from django.http import Http404
from other_app.models import Sliders
from admin_panel.serializer.sliders import SlidersAdminSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import django_filters


class SlidersFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Sliders
        fields = ['title']


# Create (Yaratish)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_slider(request):
    serializer = SlidersAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_sliders(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    sliders = Sliders.objects.all().order_by("id")
    sliders_filter = SlidersFilter(request.GET, queryset=sliders)
    result_page = paginator.paginate_queryset(sliders_filter.qs, request)
    serializer = SlidersAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def sliders_detail(request, pk):
    try:
        slider = Sliders.objects.get(pk=pk)
    except Sliders.DoesNotExist:
        raise Http404

    serializer = SlidersAdminSerializer(slider)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_slider(request, pk):
    try:
        slider = Sliders.objects.get(pk=pk)
    except Sliders.DoesNotExist:
        return Response({'error': 'Slider not found'}, status=404)

    serializer = SlidersAdminSerializer(slider, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_slider(request, pk):
    try:
        slider = Sliders.objects.get(pk=pk)
    except Sliders.DoesNotExist:
        return Response({'error': 'Slider not found'}, status=404)

    slider.delete()
    return Response(status=204)
