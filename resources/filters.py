import django_filters

from resources.models import Category, PeriodFilter, FilterCategories, Filters, Province, Resource


class CategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    order = django_filters.CharFilter(field_name='order',
                                      lookup_expr='icontains')  # content nomli maydon uchun filtirlash

    class Meta:
        model = Category
        fields = ['title', 'order']


class PeriodFilterSubFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = PeriodFilter
        fields = ['title', ]


class FilterCategoriesSubFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = FilterCategories
        fields = ['title', ]


class FiltersSubFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Filters
        fields = ['title', ]


class ProvinceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Province
        fields = ['title', ]


class ResourceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

    class Meta:
        model = Resource
        fields = ['title', 'content',]


