# coding: utf-8
from rest_framework import routers
from .views import SubjectViewSet

router = routers.DefaultRouter()
router.register('subjects', SubjectViewSet)
