from rest_framework.routers import DefaultRouter

from api.v1.views import (
    ConfigurationViewSet,
    DataPlanViewSet,
    DataSubscriptionViewSet,
    ProductViewSet,
    SalesRepViewSet,
    SalesRepDataSubscriptionViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register(r'salesrep', SalesRepViewSet, base_name='salesrep')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'config', ConfigurationViewSet, base_name='config')
router.register(r'dataplan', DataPlanViewSet, base_name='dataplan')
router.register(r'sub', DataSubscriptionViewSet, base_name='sub')
router.register(
    r'salesrep-sub', SalesRepDataSubscriptionViewSet, base_name='salesrep-sub')
router.register(r'product', ProductViewSet, base_name='product')
urlpatterns = router.urls
