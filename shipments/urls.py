from rest_framework.routers import DefaultRouter
from .views import ShipmentStatusViewSet

router = DefaultRouter()
router.register(r'shipments', ShipmentStatusViewSet)

urlpatterns = router.urls