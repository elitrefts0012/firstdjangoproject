from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Box, LeaderBoardRecord
from api.serializers import BoxSerializer, LeaderBoardRecordSerializer


class LeaderBoardRecordViewSet(viewsets.ModelViewSet):
    queryset = LeaderBoardRecord.objects.all()
    serializer_class = LeaderBoardRecordSerializer
    permission_classes = (AllowAny,)


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = (AllowAny,)
