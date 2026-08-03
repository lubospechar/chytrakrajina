from rest_framework.routers import DefaultRouter

from catalogue.api.views import MeasureGroupViewSet, MeasureViewSet

router = DefaultRouter()
router.register("measure-groups", MeasureGroupViewSet, basename="measure-group")
router.register("measures", MeasureViewSet, basename="measure")
urlpatterns = router.urls
