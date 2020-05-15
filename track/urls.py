from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shoot/(\w+)$', views.shoot, name='shoot'),
    path('track/', views.TrackList.as_view()),
    path('track/<uuid:pk>/', views.TrackDetail.as_view()),
]