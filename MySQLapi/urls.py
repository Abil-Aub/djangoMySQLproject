from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapi, name='myapi'),
    path('<str:agen>/', views.myapi_agen, name='myapi_agen'),
    path('<int:year>/<int:month>/<int:day>/', views.myapi_date, name='myapi_date'),
    path('<int:year>/<int:month>/<int:day>/<str:agen>/', views.myapi_date_agen, name='myapi_date_agen'),
]
