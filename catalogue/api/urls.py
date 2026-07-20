from rest_framework.routers import DefaultRouter

from catalogue.api.views import MeasureGroupViewSet

router = DefaultRouter()
router.register("measure-groups", MeasureGroupViewSet, basename="measure-group")

urlpatterns = router.urls