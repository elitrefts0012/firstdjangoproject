from rest_framework import serializers

from api.models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = (
            'box_id',
            'horizontal_velocity',
            'vertical_velocity',
            'distance_top',
            'distance_left',
            'color',
            'size',
        )
