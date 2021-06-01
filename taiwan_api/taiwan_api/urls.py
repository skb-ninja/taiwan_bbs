from os import name
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bbs import views

router = DefaultRouter()
router.register('subjects', views.SubjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name="api")
]
