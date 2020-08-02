from rest_framework import serializers

from api.models import Box, LeaderBoardRecord


class LeaderBoardRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardRecord
        fields = (
            'id',
            'player_username',
            'time_seconds',
            'time_minutes',
            'time_hundredths',
        )


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = (
            'id',
            'horizontal_velocity',
            'vertical_velocity',
            'distance_top',
            'distance_left',
            'color',
            'size',
        )
