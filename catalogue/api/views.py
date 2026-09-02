from rest_framework import viewsets
from django.utils.translation import get_language, activate

from catalogue.models import (
    MeasureGroup,
    Measure,
    LocationType,
    Limitation,
    AdvatageCategory,
    Advantage, SDG,
)
from catalogue.api.serializers import (
    MeasureGroupSerializer,
    MeasureSerializer,
    LocationTypeSerializer,
    LimitationSerializer,
    AdvantageCategorySerializer,
    AdvantageSerializer, SDGSerializer,
)


class MeasureGroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Measure groups.
    """

    queryset = MeasureGroup.objects.all()
    serializer_class = MeasureGroupSerializer
    lookup_field = "uuid"

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)


class MeasureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Measures.
    """

    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    lookup_field = "uuid"

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)


class LocationTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Location types.
    """

    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    lookup_field = "uuid"
    pagination_class = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)


class LimitationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Limitations.
    """

    queryset = Limitation.objects.all()
    serializer_class = LimitationSerializer
    lookup_field = "uuid"
    pagination_class = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)


class AdvantageCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Advantage categories.
    """

    queryset = AdvatageCategory.objects.all()
    serializer_class = AdvantageCategorySerializer
    lookup_field = "uuid"
    pagination_class = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)


class AdvantageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Advantages.
    """

    queryset = Advantage.objects.select_related("advantage_category").all()
    serializer_class = AdvantageSerializer
    lookup_field = "uuid"
    pagination_class = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)


class SDGViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only API for Sustainable Development Goals (SDG).
    """

    queryset = SDG.objects.all().order_by("sdg_number")
    serializer_class = SDGSerializer
    lookup_field = "uuid"
    pagination_class = None  # Cílů SDG je fixní počet (17), stránkování obvykle není nutné

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        language_code = getattr(
            request,
            "LANGUAGE_CODE",
        )
        activate(language_code)