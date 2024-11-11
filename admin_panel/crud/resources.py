from rest_framework.decorators import api_view
from rest_framework.response import Response

from admin_panel.serializer.resources import CategoryAdminSerializer, PeriodFilterAdminSerializer, \
    FilterCategoriesAdminSerializer, FiltersAdminSerializer, ProvinceAdminSerializer, ResourceAdminSerializer
from resources.filters import CategoryFilter, PeriodFilterSubFilter, FilterCategoriesSubFilter, FiltersSubFilter, \
    ProvinceFilter, ResourceFilter
from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource
from rest_framework.pagination import PageNumberPagination



@api_view(['GET'])
def categoryList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100
    cats = Category.objects.all().order_by("id")
    cat__filter = CategoryFilter(request.GET, queryset=cats)
    result_page = paginator.paginate_queryset(cat__filter.qs, request)
    serializer = CategoryAdminSerializer(result_page, many=True, context={'request': request}).data

    for data in serializer:
        if data.get('icon'):
            data['icon'] = request.build_absolute_uri(data['icon'])

    return paginator.get_paginated_response(serializer)


@api_view(['GET'])
def categoryDetail(request, pk):
    cat = Category.objects.get(pk=pk)
    serializer = CategoryAdminSerializer(cat, many=False)
    serialized_data = serializer.data

    # Rasmning URL manzilini qo'shib ko'ramiz
    if serialized_data.get('icon'):
        serialized_data['icon'] = request.build_absolute_uri(serialized_data['icon'])

    return Response(serialized_data)


@api_view(['POST'])
def createCategory(request):
    serializer = CategoryAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateCategory(request, pk):
    try:
        cat = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    serializer = CategoryAdminSerializer(cat, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deleteCategory(request, pk):
    try:
        cat = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    cat.delete()
    return Response(status=204)


@api_view(['GET'])
def periodFilterList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100
    period_filter = PeriodFilter.objects.all().order_by('id')
    search_filter = PeriodFilterSubFilter(request.GET,queryset=period_filter)
    result_page = paginator.paginate_queryset(search_filter.qs, request)
    serializer = PeriodFilterAdminSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])
def periodFilterDetail(request, pk):
    periodfilter = PeriodFilter.objects.get(pk=pk)
    serializer = PeriodFilterAdminSerializer(periodfilter, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createPeriodFilter(request):
    serializer = PeriodFilterAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updatePeriodFilter(request, pk):
    try:
        periodfilter = PeriodFilter.objects.get(pk=pk)
    except PeriodFilter.DoesNotExist:
        return Response({'error': 'PeriodFilter not found'}, status=404)

    serializer = PeriodFilterAdminSerializer(periodfilter, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deletePeriodFilter(request, pk):
    try:
        periodfilter = PeriodFilter.objects.get(pk=pk)
    except PeriodFilter.DoesNotExist:
        return Response({'error': 'PeriodFilter not found'}, status=404)

    periodfilter.delete()
    return Response(status=204)


@api_view(['GET'])
def filterCategoriesList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100

    filter_categories = FilterCategories.objects.all()
    filter_sub = FilterCategoriesSubFilter(request.GET,queryset=filter_categories)
    result_page = paginator.paginate_queryset(filter_sub.qs, request)

    serializer = FilterCategoriesAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def filterCategoriesDetail(request, pk):
    filter_categories = FilterCategories.objects.get(pk=pk)
    serializer = FilterCategoriesAdminSerializer(filter_categories, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createFilterCategories(request):
    serializer = FilterCategoriesAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)




@api_view(['PUT'])
def updateFilterCategories(request, pk):
    try:
        filter_categories = FilterCategories.objects.get(pk=pk)
    except FilterCategories.DoesNotExist:
        return Response({'error': 'FilterCategories not found'}, status=404)

    serializer = FilterCategoriesAdminSerializer(filter_categories, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deleteFilterCategories(request, pk):
    try:
        filter_categories = FilterCategories.objects.get(pk=pk)
    except FilterCategories.DoesNotExist:
        return Response({'error': 'FilterCategories not found'}, status=404)

    filter_categories.delete()
    return Response(status=204)


@api_view(['GET'])
def filtersList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100

    filters = Filters.objects.all().order_by('id')
    filter_sub = FiltersSubFilter(request.GET, queryset=filters)
    result_page = paginator.paginate_queryset(filter_sub.qs, request)

    serializer = FiltersAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def filtersDetail(request, pk):
    filters = Filters.objects.get(pk=pk)
    serializer = FiltersAdminSerializer(filters, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createFilters(request):
    serializer = FiltersAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateFilters(request, pk):
    try:
        filters = Filters.objects.get(pk=pk)
    except Filters.DoesNotExist:
        return Response({'error': 'Filters not found'}, status=404)

    serializer = FiltersAdminSerializer(filters, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deleteFilters(request, pk):
    try:
        filters = Filters.objects.get(pk=pk)
    except Filters.DoesNotExist:
        return Response({'error': 'Filters not found'}, status=404)

    filters.delete()
    return Response(status=204)


@api_view(['GET'])
def provinceList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100
    provinces = Province.objects.all().order_by('id')
    provinces_filter = ProvinceFilter(request.GET, queryset=provinces)
    result_page = paginator.paginate_queryset(provinces_filter.qs, request)
    serializer = ProvinceAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def provinceDetail(request, pk):
    province = Province.objects.get(pk=pk)
    serializer = ProvinceAdminSerializer(province, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProvince(request):
    serializer = ProvinceAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateProvince(request, pk):
    try:
        province = Province.objects.get(pk=pk)
    except Province.DoesNotExist:
        return Response({'error': 'Province not found'}, status=404)

    serializer = ProvinceAdminSerializer(province, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deleteProvince(request, pk):
    try:
        province = Province.objects.get(pk=pk)
    except Province.DoesNotExist:
        return Response({'error': 'Province not found'}, status=404)

    province.delete()
    return Response(status=204)


@api_view(['GET'])
def resourceList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    resources = Resource.objects.all().order_by('id')
    resourcec_filter = ResourceFilter(request.GET,queryset=resources)
    result_page = paginator.paginate_queryset(resourcec_filter.qs, request)
    serializer = ResourceAdminSerializer(result_page, many=True)
    serialized_data = serializer.data
    for data in serialized_data:
        if data.get('image'):
            data['image'] = request.build_absolute_uri(data['image'])
        if data.get('interive_list'):
            for interive in data['interive_list']:
                if interive.get('file'):
                    interive['file'] = request.build_absolute_uri(interive['file'])
    return paginator.get_paginated_response(serialized_data)


@api_view(['GET'])
def resourceDetail(request, pk):
    resource = Resource.objects.get(pk=pk)
    serializer = ResourceAdminSerializer(resource, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createResource(request):
    serializer = ResourceAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateResource(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response({'error': 'Resource not found'}, status=404)

    serializer = ResourceAdminSerializer(resource, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)





@api_view(['DELETE'])
def deleteResource(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response({'error': 'Resource not found'}, status=404)

    resource.delete()
    return Response(status=204)




