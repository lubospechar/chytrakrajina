from rest_framework import serializers

from catalogue.models import MeasureGroup


class MeasureGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureGroup
        fields = (
            "uuid",
            "name",
            "description",
            "icon",
        )