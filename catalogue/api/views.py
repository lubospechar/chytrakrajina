
from rest_framework import viewsets
from django.utils.translation import get_language, activate

from catalogue.models import MeasureGroup
from catalogue.api.serializers import MeasureGroupSerializer


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
