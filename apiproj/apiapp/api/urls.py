from django.urls import path 
from . import apiviews
from .apiviews import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns =[
    path('register/',apiviews.registerAPIView.as_view(),name = 'login'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getall/',apiviews.getall,name = 'getall'),
    path('getuser/<str:pk>',apiviews.getuser,name = 'dispuser'),
    path('assigntask/<str:pk1>',apiviews.assigntask,name = 'assign'),
    path('apiviewuser/',apiviews.UserAPIView.as_view(),name = 'APIVIEWS'),
    path('infodata/<int:pk>',apiviews.infodataAPIView.as_view(),name = 'infodataview'),
    path('taskapi/',apiviews.taskAPIView.as_view(),name = 'tasks'),
    path('updatetask/<int:pk>',apiviews.taskupdateAPIView.as_view(),name = 'updatetask'),
]