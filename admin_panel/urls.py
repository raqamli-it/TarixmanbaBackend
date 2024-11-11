from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
# library 
from admin_panel.crud.library import create_library, library_detail, list_libraries, delete_library, update_library
# library_cat 
from admin_panel.crud.library_category import create_library_category, library_category_detail, list_library_categories, update_library_category, delete_library_category
# news
from admin_panel.crud.news import  list_news, create_news, news_detail, update_news, delete_news

from admin_panel.crud.resources import  categoryList, createCategory, categoryDetail, updateCategory, deleteCategory \

from admin_panel.crud.resources import  categoryList, createCategory, categoryDetail, updateCategory, \
    deleteCategory, \
    periodFilterList, periodFilterDetail, updatePeriodFilter, deletePeriodFilter, createPeriodFilter, \
    filterCategoriesList, filterCategoriesDetail, createFilterCategories, updateFilterCategories, \
    deleteFilterCategories, filtersList, filtersDetail, createFilters, updateFilters, deleteFilters, provinceList, \
    provinceDetail, createProvince, updateProvince, deleteProvince, resourceList, resourceDetail, createResource, \
    updateResource, deleteResource
# sliders 
from admin_panel.crud.sliders import list_sliders, create_slider, sliders_detail, update_slider, delete_slider
# connection 
from admin_panel.crud.connection import connection_detail, list_connections,  create_connection, delete_connection,  update_connection
# about 
from admin_panel.crud.about import create_about, update_about, delete_about, list_abouts, about_detail
# feedback
from admin_panel.crud.feedback import feedbacks_detail, list_feedbacks, create_feedback, update_feedback, delete_feedback
# comment 
from admin_panel.crud.comment import create_comment, update_comment, list_comments, delete_comment, comment_detail
# resource 
# connection_category
from admin_panel.crud.connection_category import connection_category_detail, create_connection_category, delete_connection_category, list_connection_category, update_connection_category
# connection_value 
from admin_panel.crud.connection_value import connection_value_detail, create_connection_value, delete_connection_value, list_connection_value, update_connection_value


urlpatterns = [
    path('library_category/', list_library_categories, name='list_library_categories'),
    path('library_category/create/', create_library_category, name='create_library_category'),
    path('library_category/<int:pk>/update/', update_library_category, name='update_library_category'),
    path('library_category/<int:pk>/delete/', delete_library_category, name='delete_library_category'),
    path('library-categories/<int:pk>/detail/', library_category_detail, name='library-category-detail'),




    # Library 
    path('library/', list_libraries, name='list_libraries'),
    path('library/create/', create_library, name='create_library'),
    path('library/<int:pk>/update/', update_library, name='update_library'),
    path('library/<int:pk>/delete/', delete_library, name='delete_library'),
    path('libraries/<int:pk>/detail/', library_detail, name='library-detail'),




    # News
    path('news/', list_news, name='list_news'),
    path('news/create/', create_news, name='create_news'),
    path('news/<int:pk>/update/', update_news, name='update_news'),
    path('news/<int:pk>/delete/', delete_news, name='delete_news'),
    path('news/<int:pk>/detail/', news_detail, name='news-detail'),



    
    # sliders
    path('sliders/', list_sliders, name='list_sliders'),
    path('sliders/create/', create_slider, name='create_slider'),
    path('sliders/<int:pk>/update/', update_slider, name='update_slider'),
    path('sliders/<int:pk>/delete/', delete_slider, name='delete_slider'),
    path('sliders/<int:pk>/detail/', sliders_detail, name='sliders-detail'),



    # connection 
    path('connections/', list_connections, name='list-connections'),
    path('connections/create/', create_connection, name='create-connection'),
    path('connections/<int:pk>/update/', update_connection, name='update-connection'),
    path('connections/<int:pk>/delete/', delete_connection, name='delete-connection'),
    path('connection/<int:pk>/detail/', connection_detail, name='connection-detail'),



    # About 
    path('about/', list_abouts, name='list_abouts'),
    path('about/create/', create_about, name='create_about'),
    path('about/<int:pk>/update/', update_about, name='update_about'),
    path('about/<int:pk>/delete/', delete_about, name='delete_about'),
    path('about/<int:pk>/detail/', about_detail, name='about-detail'),



    # Feedback
    path('feedback/', list_feedbacks, name='list_feedbacks'),
    path('feedback/create/', create_feedback, name='create_feedback'),
    path('feedback/<int:pk>/update/', update_feedback, name='update_feedback'),
    path('feedback/<int:pk>/delete/', delete_feedback, name='delete_feedback'),
    path('feedbacks/<int:pk>/detail/', feedbacks_detail, name='feedbacks-detail'),




    # Comment
    path('comment/', list_comments, name='list_comments'),
    path('comment/create/', create_comment, name='create_comment'),
    path('comment/<int:pk>/update/', update_comment, name='update_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
    path('comment/<int:pk>/detail/', comment_detail, name='comment-detail'),


    #Resource   category
    path('category/',categoryList,name='cat-list'),
    path('category/<int:pk>/detail/',categoryDetail,name='cat-detail'),
    path('category/<int:pk>/update/',updateCategory,name='cat-update'),
    path('category/<int:pk>/delete/',deleteCategory,name='cat-delete'),
    path('category/create/',createCategory,name='cat-create'),

    # Resource periodfilter
    path('period_filter/',periodFilterList,name='period-filter-list'),
    path('period_filter/<int:pk>/detail/',periodFilterDetail,name='period-filter-detail'),
    path('period_filter/<int:pk>/update/',updatePeriodFilter,name='period-filter-update'),
    path('period_filter/<int:pk>/delete/',deletePeriodFilter,name='period-filter-delete'),
    path('period_filter/create/',createPeriodFilter,name='period-filter-create'),

    # Resource filter-category
    path('filter_category/', filterCategoriesList, name='filter-category-list'),
    path('filter_category/<int:pk>/detail/', filterCategoriesDetail, name='filter-category-detail'),
    path('filter_category/create/', createFilterCategories, name='filter-category-create'),
    path('filter_category/<int:pk>/update/', updateFilterCategories, name='filter-category-update'),
    path('filter_category/<int:pk>/delete/', deleteFilterCategories, name='filter-category-delete'),

    # Resource filters
    path('filters/', filtersList, name='filters-list'),
    path('filters/<int:pk>/detail/', filtersDetail, name='filters-detail'),
    path('filters/create/', createFilters, name='filters-create'),
    path('filters/<int:pk>/update/', updateFilters, name='filters-update'),
    path('filters/<int:pk>/delete/', deleteFilters, name='filters-delete'),

    # Resource province
    path('province/', provinceList, name='province-list'),
    path('province/<int:pk>/detail/', provinceDetail, name='province-detail'),
    path('province/create/', createProvince, name='province-create'),
    path('province/<int:pk>/update/', updateProvince, name='province-update'),
    path('province/<int:pk>/delete/', deleteProvince, name='province-delete'),

    # Resource
    path('resource/', resourceList, name='resource-list'),
    path('resource/<int:pk>/detail/', resourceDetail, name='resource-detail'),
    path('resource/create/', createResource, name='resource-create'),
    path('resource/<int:pk>/update/', updateResource, name='resource-update'),
    path('resource/<int:pk>/delete/', deleteResource, name='resource-delete'),

    # Connection-category
    path('connection_category/', list_connection_category, name='connectin-category-list'),
    path('connection_category/<int:pk>/detail/', connection_category_detail, name='connectin-category-detail'),
    path('connection_category/create/', create_connection_category, name='connectin-category-create'),
    path('connection_category/<int:pk>/update/', update_connection_category, name='connectin-category-update'),
    path('connection_category/<int:pk>/delete/', delete_connection_category, name='connectin-category-delete'),

    # Connection-value
    path('connection_value/', list_connection_value, name='connectin-value-list'),
    path('connection_value/<int:pk>/detail/', connection_value_detail, name='connectin-value-detail'),
    path('connection_value/create/', create_connection_value, name='connectin-value-create'),
    path('connection_value/<int:pk>/update/', update_connection_value, name='connectin-value-update'),
    path('connection_value/<int:pk>/delete/', delete_connection_value, name='connectin-value-delete'),


    
]
