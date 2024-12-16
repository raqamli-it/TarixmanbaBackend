from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import F

# from admin_panel.serializer.resources import ResourceAdminSerializer
from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource, Location
from resources.serializer import CategorySerializer, PeriodFilterSerializer, FilterCategoriesSerializer, \
    FiltersSerializer, ProvinceSerializer, ResourceSerializer, CategoryResourceSerializer, LocationSerializer, CategoryResourceListSerializer


@api_view(['GET'])
def categoryListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    cats = Category.objects.all().prefetch_related('resources').order_by('order')
    result_page = paginator.paginate_queryset(cats, request)
    serializer = CategoryResourceSerializer(result_page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def categoryDetailView(request, pk):
    cat = Category.objects.get(pk=pk)
    serializer = CategorySerializer(cat, many=False, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def periodFilterListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    period_filter = PeriodFilter.objects.all()
    result_page = paginator.paginate_queryset(period_filter, request)
    serializer = PeriodFilterSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def periodFilterDetailView(request, pk):
    period_filter = PeriodFilter.objects.get(pk=pk)
    serializer = PeriodFilterSerializer(period_filter, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def filterCategoriesListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    filter_categories = FilterCategories.objects.all()
    result_page = paginator.paginate_queryset(filter_categories, request)

    serializer = FilterCategoriesSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def filterCategoriesDetailView(request, pk):
    filter_categories = FilterCategories.objects.get(pk=pk)
    serializer = FilterCategoriesSerializer(filter_categories, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def filtersListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    filters = Filters.objects.all()
    result_page = paginator.paginate_queryset(filters, request)

    serializer = FiltersSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def filtersDetailView(request, pk):
    filters = Filters.objects.get(pk=pk)
    serializer = FiltersSerializer(filters, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def provinceListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    provinces = Province.objects.all()
    result_page = paginator.paginate_queryset(provinces, request)
    serializer = ProvinceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def provinceDetailView(request, pk):
    province = Province.objects.get(pk=pk)
    serializer = ProvinceSerializer(province, many=False)
    return Response(serializer.data)


# @api_view(['GET'])
# def resourceListView(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = 10
#     resources = Resource.objects.all()
#     result_page = paginator.paginate_queryset(resources, request)
#     serializer = ResourceSerializer(result_page, context={'request': request}, many=True)
#     serialized_data = serializer.data
#     for data in serialized_data:
#         if data.get('image'):
#             data['image'] = request.build_absolute_uri(data['image'])
#     return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def resourceListView(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10

    # select_related va prefetch_related yordamida resurslarni oldindan yuklash
    resources = Resource.objects.select_related('category', 'filter_category') \
                                .prefetch_related(
                                    'files', 'audios', 'videos', 'galleries', 'attributes', 'contents', 'virtual_realities', 'locations'
                                )
    result_page = paginator.paginate_queryset(resources, request)
    serializer = ResourceSerializer(result_page, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def resourceDetailView(request, pk):
    resource = Resource.objects.get(pk=pk)
    serializer = ResourceSerializer(resource, context={'request': request}, many=False)
    serialized_data = serializer.data

    if serialized_data.get('image'):
        serialized_data['image'] = request.build_absolute_uri(serialized_data['image'])

    return Response(serialized_data)


@api_view(['GET'])
def catResourceListView(request):
    category = Category.objects.all().order_by(F('order').asc(nulls_last=True))
    serializer = CategoryResourceListSerializer(category, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def catResourceDetailView(request, pk):
    # Get the category object
    category = get_object_or_404(Category, pk=pk)

    # Get query parameters
    period_filter_id = request.GET.get('period_filter')
    filter_ids = request.GET.getlist('filters')  # Expecting a list of filter IDs

    # Filter by period_filter if provided
    if period_filter_id:
        period_filter = PeriodFilter.objects.filter(id=period_filter_id, category=category).first()
        if period_filter:
            resources = Resource.objects.filter(
                category=category, period_filter=period_filter
                ).select_related(
                    'category', 'filter_category'
                    ).prefetch_related(
                        'files', 'audios', 'videos', 'galleries', 'attributes', 
                        'contents', 'virtual_realities', 'locations'
                        )
        else:
            resources = Resource.objects.none()  # No matching filter found
    else:
        resources = Resource.objects.filter(
            category=category
            ).select_related(
                    'category', 'filter_category'
                    ).prefetch_related(
                        'files', 'audios', 'videos', 'galleries', 'attributes', 
                        'contents', 'virtual_realities', 'locations'
                        )


    # Further filter by filters if provided
    if filter_ids:
        resources = resources.filter(filters__id__in=filter_ids).distinct()

    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_resources = paginator.paginate_queryset(resources, request)
    resource_serializer = ResourceSerializer(paginated_resources, context={'request': request}, many=True)

    serialized_data = resource_serializer.data

    # Serialize period filters data
    period_filters = PeriodFilter.objects.filter(category=category)
    period_filter_serializer = PeriodFilterSerializer(period_filters, many=True, context={'request': request})

    # Serialize filter categories data
    filter_categories = FilterCategories.objects.filter(category=category)
    filter_category_serializer = FilterCategoriesSerializer(filter_categories, many=True, context={'request': request})

    # Serialize filters data
    filters = Filters.objects.filter(filter_category__in=filter_categories)
    filter_serializer = FiltersSerializer(filters, many=True, context={'request': request})

    # Prepare response data
    response_data = {
        'category': category.title,
        'period_filters': period_filter_serializer.data,
        'filter_categories': filter_category_serializer.data,
        'filters': filter_serializer.data,

    }
    response_data['resources'] = paginator.get_paginated_response(serialized_data).data
    return Response(response_data)


# behruz
@api_view(['GET'])
def category_locations_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)

    locations = Location.objects.filter(resource__category=category)
    serializer = LocationSerializer(locations, many=True, context={'request': request})
    return Response(serializer.data)
