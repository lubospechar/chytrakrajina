from rest_framework import serializers

from catalogue.models import (
    Measure,
    MeasureGroup,
    LocationType,
    Advantage,
    MainProblems,
    Limitation,
    FundingOpportunity,
    SDG,
    Law,
)


class MeasureGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureGroup
        fields = (
            "uuid",
            'slug',
            "ordering",
            "name",
            "short_name",
            "description",
            "icon",
            'created_at',
            'last_modified',
            'measure_count',
        )


class UUIDNameRelatedSerializer(serializers.Serializer):
    """
    Generic helper serializer for M2M relations - returns UUID
    together with the string representation of the related object.
    """
    uuid = serializers.UUIDField()
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return str(obj)

class MeasureCombineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ("uuid", "name",)

class MeasureSerializer(serializers.ModelSerializer):
    groups = UUIDNameRelatedSerializer(many=True, read_only=True)
    location_type = UUIDNameRelatedSerializer(many=True, read_only=True)
    main_advantage = UUIDNameRelatedSerializer(many=True, read_only=True)
    advantage = UUIDNameRelatedSerializer(many=True, read_only=True)
    main_problems = UUIDNameRelatedSerializer(many=True, read_only=True)
    limitation = UUIDNameRelatedSerializer(many=True, read_only=True)
    funding_opportunity = UUIDNameRelatedSerializer(many=True, read_only=True)
    combine = MeasureCombineSerializer(many=True, read_only=True)
    sdg = UUIDNameRelatedSerializer(many=True, read_only=True)
    law = UUIDNameRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Measure
        fields = (
            "uuid",
            "name",
            "slug",
            "created_at",
            "last_modified",
            "groups",
            "location_type",
            "short_description",
            "description",
            "when_and_why_to_use",
            "purpose",
            "temperature",
            "water",
            "biodiversity",
            "air",
            "aesthetics",
            "main_advantage",
            "advantage",
            "municipality_size",
            "main_problems",
            "limitation",
            "complexity_of_realization",
            "budget_choices",
            "funding_opportunity",
            "price",
            "units",
            "time_horizon",
            "measure_size",
            "diy",
            "combine",
            "sdg",
            "law",
        )