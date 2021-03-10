from django.urls import path
from .views import circle_list_view,circle_detail_view, circle_edit_view, circle_like_unlike, circle_search_view

app_name = 'circle'
urlpatterns = [
    path('', circle_list_view, name='main-circle-view'),
    path('liked/', circle_like_unlike, name='like-circle-view'),
    path('search/', circle_search_view, name='search-circle-view'),
    path('<slug:slug>/', circle_detail_view, name='detail-circle-view'),
    path('<slug:slug>/edit/', circle_edit_view),
]
