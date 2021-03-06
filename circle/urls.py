from django.urls import path
from .views import circle_list_view,circle_detail_view, circle_edit_view

urlpatterns = [
    path('', circle_list_view),
    path('<slug:slug>/', circle_detail_view),
    path('<slug:slug>/edit/', circle_edit_view),
]
