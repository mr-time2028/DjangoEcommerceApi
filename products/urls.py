from .views import PorductViewSet
from rest_framework.routers import DefaultRouter

app_name = 'products'
router = DefaultRouter()
router.register(r'', PorductViewSet, basename='product-list')   # list of all products API url router
urlpatterns = router.urls