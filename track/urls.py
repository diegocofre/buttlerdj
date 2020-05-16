from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shoot/(\w+)$', views.shoot, name='shoot'),
    path('track/', views.TrackList.as_view()),
    path('track/<uuid:pk>/', views.TrackDetail.as_view()),
    path('segment/', views.SegmentList.as_view()),
    path('segment/<uuid:pk>/', views.SegmentDetail.as_view()),
    path('milestone/', views.MilestoneList.as_view()),
    path('milestone/<uuid:pk>/', views.MilestoneDetail.as_view()),
]