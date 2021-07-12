from django.urls import path
from .views import AdList, AdDetail

urlpatterns = [
    path('ad', AdList.as_view(), name='ad_list_view'),
    path('ad/<int:pk>', AdDetail.as_view(), name='ad_detail_view'),
]