from rest_framework import serializers

from catalogue.models import MeasureGroup


class MeasureGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureGroup
        fields = (
            "uuid",
            'slug',
            "name",
            "description",
            "icon",
            'created_at',
            'last_modified',
        )