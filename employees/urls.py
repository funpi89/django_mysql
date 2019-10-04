from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_all, name='show_all'),
    path('all_api',views.show_all_api, name='show_all_api'),
    path('query',views.query, name='query'),
    path('query_api',views.query_api, name='query_api'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]