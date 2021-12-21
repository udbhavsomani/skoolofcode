from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('addsubject', SubjectViewSet, basename='subject')
router.register('users', UserViewSet)
router.register('availabletiming', AvailableTimingViewSet, basename='availableTiming')

urlpatterns = [
    path('api/', include(router.urls)),
    path('get_subs/', get_subs, name='get_subs'),
    path('get_query_results/', get_query_results, name='get_query_results'),
]