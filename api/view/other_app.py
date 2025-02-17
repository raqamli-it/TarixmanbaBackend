from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from admin_panel.crud.about import AboutFilter
from admin_panel.crud.connection_value import ConnectionValFilter
from admin_panel.crud.feedback import FeedbackFilter
from admin_panel.crud.library import LibraryFilter
from admin_panel.crud.library_category import LibraryCatFilter
from admin_panel.crud.news import NewsFilter
from admin_panel.crud.sliders import SlidersFilter
from other_app.models import About, Connection_Value, Feedbacks, Library_Category, Library, \
    Sliders, News, Employee
from other_app.serializers import AboutSerializer, ConnectionValueSerializer, \
    FeedbackSerializer, LibrariesSerializer, NewsSerializer, LibrariesCategorySerializer, SlidersSerializer, \
    EmployeeListSerializer
from rest_framework.pagination import PageNumberPagination


# Library

# Read (O'qish)
@api_view(['GET'])
def list_libraries(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    library_filter = LibraryFilter(request.GET, queryset=Library.objects.all().order_by("id"))
    result_page = paginator.paginate_queryset(library_filter.qs, request)
    serializer = LibrariesSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Detail
@api_view(['GET'])
def library_detail(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        raise Http404

    serializer = LibrariesSerializer(library)
    return Response(serializer.data)


# Library category

# Read (O'qish)
@api_view(['GET'])
def list_library_categories(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    library_cat__filter = LibraryCatFilter(request.GET, queryset=Library_Category.objects.all().order_by("id"))
    result_page = paginator.paginate_queryset(library_cat__filter.qs, request)
    serializer = LibrariesCategorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Detail
@api_view(['GET'])
def library_category_detail(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        raise Http404

    serializer = LibrariesCategorySerializer(category)
    return Response(serializer.data)


# About

# Read (O'qish)
@api_view(['GET'])
def list_abouts(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    about_filter = AboutFilter(request.GET, queryset=About.objects.all().order_by("id"))
    result_page = paginator.paginate_queryset(about_filter.qs, request)
    serializer = AboutSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Detail
@api_view(['GET'])
def about_detail(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        raise Http404

    serializer = AboutSerializer(about)
    return Response(serializer.data)


# News
# Read (O'qish)
@api_view(['GET'])
def list_news(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    news_filter = NewsFilter(request.GET, queryset=News.objects.all().order_by("id"))
    result_page = paginator.paginate_queryset(news_filter.qs, request)
    serializer = NewsSerializer(result_page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


# Detail
@api_view(['GET'])
def news_detail(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        raise Http404

    serializer = NewsSerializer(news, context={'request': request})
    return Response(serializer.data)


# Read (O'qish)
# @api_view(['GET'])
# def list_sliders(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = 20
#     sliders = Sliders.objects.all().order_by("id")
#     sliders_filter = SlidersFilter(request.GET, queryset=sliders)
#     result_page = paginator.paginate_queryset(sliders_filter.qs, request)
#     serializer = SlidersSerializer(result_page, many=True)
#     return paginator.get_paginated_response(serializer.data)

# # Detail
# @api_view(['GET'])
# def sliders_detail(request, pk):
#     try:
#         slider = Sliders.objects.get(pk=pk)
#     except Sliders.DoesNotExist:
#         raise Http404

#     serializer = SlidersSerializer(slider)
#     return Response(serializer.data)

@api_view(['GET'])
def list_sliders(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    sliders_filter = SlidersFilter(request.GET, queryset=Sliders.objects.all().order_by("id"))
    result_page = paginator.paginate_queryset(sliders_filter.qs, request)
    serializer = SlidersSerializer(result_page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def sliders_detail(request, pk):
    try:
        slider = Sliders.objects.get(pk=pk)
    except Sliders.DoesNotExist:
        raise Http404

    serializer = SlidersSerializer(slider, many=False, context={'request': request})
    return Response(serializer.data)


# Read (O'qish)
@api_view(['GET'])
def list_connection_value(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    connections_val_filter = ConnectionValFilter(request.GET, queryset=Connection_Value.objects.all().order_by("id"))
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


# feedbacks
# Read (O'qish)
@api_view(['GET'])
def list_feedbacks(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    feedback_filter = FeedbackFilter(request.GET, queryset=Feedbacks.objects.all().order_by("id"))
    result_page = paginator.paginate_queryset(feedback_filter.qs, request)
    serializer = FeedbackSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Detail
@api_view(['GET'])
def feedbacks_detail(request, pk):
    try:
        feedback = Feedbacks.objects.get(pk=pk)
    except Feedbacks.DoesNotExist:
        raise Http404

    serializer = FeedbackSerializer(feedback)
    return Response(serializer.data)


@api_view(['GET'])
def list_employee(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    connections_val_filter = ConnectionValFilter(request.GET, queryset=Employee.objects.all().order_by("order"))
    result_page = paginator.paginate_queryset(connections_val_filter.qs, request)
    serializer = EmployeeListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
