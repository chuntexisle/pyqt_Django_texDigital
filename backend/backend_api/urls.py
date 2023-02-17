from django.urls import path
from . import views


urlpatterns = [
    path('lots/all', views.releasedlots_list),
    path('lots/all/<int:pk>', views.releasedlots_detail),
    path('processing/', views.ProcessingListView.as_view(), name='processing'),
    path('processing/all/<int:pk>', views.processing_detail, name='processing-detail'),
]
