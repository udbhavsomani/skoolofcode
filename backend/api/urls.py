from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('addSubject', SubjectViewSet, basename='subject')
router.register('users', UserViewSet)
router.register('addAvailableTiming', AvailableTimingViewSet, basename='availableTiming')

urlpatterns = [
    path('api/', include(router.urls)),
]