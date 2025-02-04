from django.contrib import admin
from django.urls import include, path

from .views import (DeleteClassAPIView, ShowClassesAPIView,
                    UpdateClassNameAPIView)

urlpatterns = [
    path('classes/', ShowClassesAPIView.as_view()),
    path('updateClass/<pk>/', UpdateClassNameAPIView.as_view()),
    path('deleteClass/<pk>/', DeleteClassAPIView.as_view()),
]
