from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('catalog', views.catalog),
    path('catalog/<int:page_num>', views.inf),
    path('catalog/<int:page_num>/city/<int:city_id>', views.city)
]
