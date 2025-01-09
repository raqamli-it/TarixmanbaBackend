from django.urls import path
from api.view.other_app import about_detail, connection_value_detail,  feedbacks_detail, library_category_detail, library_detail, list_abouts, list_connection_value,  list_feedbacks, list_libraries, list_library_categories, list_news, list_sliders, news_detail, sliders_detail
from api.view.resources import category_locations_view, categoryListView, categoryDetailView, periodFilterListView, periodFilterDetailView, \
    filterCategoriesListView, filterCategoriesDetailView, filtersListView, filtersDetailView, provinceListView, \
    provinceDetailView, resourceListView, resourceDetailView, catResourceListView, catResourceDetailView, SearchView

from resources.views import FilterCategoryAPIView, FiltersAPIView, PeriodFilterAPIView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),


    # Library
    path('libraries/', list_libraries, name='list_libraries'),
    path('libraries/<int:pk>/', library_detail, name='library_detail'),

    # Library Category
    path('library-categories/', list_library_categories, name='list_library_categories'),
    path('library-categories/<int:pk>/', library_category_detail, name='library_category_detail'),

    # About
    path('abouts/', list_abouts, name='list_abouts'),
    path('abouts/<int:pk>/', about_detail, name='about_detail'),


    # News
    path('news/', list_news, name='list_news'),
    path('news/<int:pk>/', news_detail, name='news_detail'),

    # # Sliders
    path('sliders/', list_sliders, name='list_sliders'),
    path('sliders/<int:pk>/', sliders_detail, name='sliders_detail'),
    # path('sliders/', SlidersListView.as_view(), name='sliders-list'),
    # path('sliders/<int:pk>/', SlidersDetailView.as_view(), name='sliders-detail'),


    # Connection Value
    path('connection-values/', list_connection_value, name='list_connection_value'),
    path('connection-values/<int:pk>/', connection_value_detail, name='connection_value_detail'),

    # Feedbacks
    path('feedbacks/', list_feedbacks, name='list_feedbacks'),
    path('feedbacks/<int:pk>/', feedbacks_detail, name='feedbacks_detail'),



    # Resources   url
    # category
    path('category_api-list/', categoryListView, name='category-list'),
    path('category_api-detail/<int:pk>/', categoryDetailView, name='category-detail'),
    # category page
    path('category-resource/', catResourceListView, name='category-res-list'),
    path('category-resource/<int:pk>/', catResourceDetailView, name='category-res-detail'),


    # period_filter
    path('period_api-list/', periodFilterListView, name='period_api-list'),
    path('period_api-detail/<int:pk>/', periodFilterDetailView, name='period_api-detail'),

    # filter_categories
    path('filter_categories_api-list/', filterCategoriesListView, name='filter_categories_api-list'),
    path('filter_categories_api-detail/<int:pk>/', filterCategoriesDetailView, name='filter_categories_api-detail'),

    # filters
    path('filters_api-list/', filtersListView, name='filters_api-list'),
    path('filters_api-detail/<int:pk>/', filtersDetailView, name='filters_api-detail'),

    # province
    path('province_api-list/', provinceListView, name='province_api-list'),
    path('province_api-detail/<int:pk>/', provinceDetailView, name='province_api-detail'),

    # resource
    path('resource_api-list/', resourceListView, name='resource_api-list'),
    path('resource_api-detail/<int:pk>/', resourceDetailView, name='resource_api-detail'),


    path("filter_category/", FilterCategoryAPIView.as_view()),
    path("filters/", FiltersAPIView.as_view()),
    path("period/", PeriodFilterAPIView.as_view()),

    
    path('categories/<int:pk>/locations/', category_locations_view, name='category-locations'),

]
