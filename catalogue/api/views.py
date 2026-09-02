from rest_framework import viewsets
from django.utils.translation import activate

from catalogue.models import (
    MeasureGroup,
    Measure,
    LocationType,
    Limitation,
    AdvatageCategory,
    Advantage,
    SDG,
)
from catalogue.api.serializers import (
    MeasureGroupSerializer,
    MeasureSerializer,
    LocationTypeSerializer,
    LimitationSerializer,
    AdvantageCategorySerializer,
    AdvantageSerializer,
    SDGSerializer,
)


class BaseLocalizedReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "uuid"

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        language_code = getattr(request, "LANGUAGE_CODE", "cs")
        if language_code:
            activate(language_code)


class MeasureGroupViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Measure groups.
    """
    queryset = MeasureGroup.objects.all()
    serializer_class = MeasureGroupSerializer


class MeasureViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Measures.
    """
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


class LocationTypeViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Location types.
    """
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    pagination_class = None


class LimitationViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Limitations.
    """
    queryset = Limitation.objects.all()
    serializer_class = LimitationSerializer
    pagination_class = None


class AdvantageCategoryViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Advantage categories.
    """
    queryset = AdvatageCategory.objects.all()
    serializer_class = AdvantageCategorySerializer
    pagination_class = None


class AdvantageViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Advantages.
    """
    queryset = Advantage.objects.select_related("advantage_category").all()
    serializer_class = AdvantageSerializer
    pagination_class = None


class SDGViewSet(BaseLocalizedReadOnlyModelViewSet):
    """
    Public read-only API for Sustainable Development Goals (SDG).
    """
    queryset = SDG.objects.all().order_by("sdg_number")
    serializer_class = SDGSerializer
    pagination_class = None