from django.http import Http404
from other_app.models import News
from admin_panel.serializer.news import NewsAdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

    class Meta:
        model = News
        fields = ['title', 'content']


# Create 
# Create (Yaratish)
# @api_view(['POST'])
# def create_news(request):
#     serializer = NewsAdminSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_news(request):
    serializer = NewsAdminSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_news(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    news = News.objects.all().order_by("id")
    news_filter = NewsFilter(request.GET, queryset=news)
    result_page = paginator.paginate_queryset(news_filter.qs, request)
    serializer = NewsAdminSerializer(result_page, many=True, context={'request': request}).data
    # return paginator.get_paginated_response(serializer.data)

    for data in serializer:
        if data.get('file'):
            data['file'] = request.build_absolute_uri(data['file'])

    return paginator.get_paginated_response(serializer)

# Detail
@api_view(['GET'])
def news_detail(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        raise Http404

    serializer = NewsAdminSerializer(news, context={'request': request})
    return Response(serializer.data)


# Update (Yangilash)
@api_view(['PUT'])
def update_news(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=404)

    serializer = NewsAdminSerializer(news, data=request.data, partial=True, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_news(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=404)

    news.delete()
    return Response(status=204)




