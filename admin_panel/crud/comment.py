from django.http import Http404
from other_app.models import Comments
from admin_panel.serializer.comment import CommentsAdminSerializer
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class CommentFilter(django_filters.FilterSet):
    message = django_filters.CharFilter(field_name='message', lookup_expr='icontains')

    class Meta:
        model = Comments
        fields = ['message']


# Create (Yaratish)
@api_view(['POST'])
def create_comment(request):
    serializer = CommentsAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_comments(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    comments = Comments.objects.all().order_by("id")
    comment_filter = CommentFilter(request.GET, queryset=comments)
    result_page = paginator.paginate_queryset(comment_filter.qs, request)
    serializer = CommentsAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def comment_detail(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        raise Http404

    serializer = CommentsAdminSerializer(comment)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_comment(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=404)

    serializer = CommentsAdminSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=404)

    comment.delete()
    return Response(status=204)
