from rest_framework import viewsets

from api.models import Box
from api.serializers import BoxSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
