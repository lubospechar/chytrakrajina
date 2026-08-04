from rest_framework.routers import DefaultRouter

from catalogue.api.views import MeasureGroupViewSet, MeasureViewSet, LocationTypeViewSet, LimitationViewSet

router = DefaultRouter()
router.register("measure-groups", MeasureGroupViewSet, basename="measure-group")
router.register("location-types", LocationTypeViewSet, basename="location-type")
router.register("limitations", LimitationViewSet, basename="limitation")
router.register("measures", MeasureViewSet, basename="measure")
urlpatterns = router.urls
