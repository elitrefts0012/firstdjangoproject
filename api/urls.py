from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api.viewsets import BoxViewSet


router = routers.DefaultRouter()
router.register('box', BoxViewSet)
urlpatterns = [
    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]