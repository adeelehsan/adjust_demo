from rest_framework.routers import DefaultRouter

from adjust_demo.records.views import RecordsViewSet

router = DefaultRouter()
router.register(r'records', RecordsViewSet, base_name='records')
urlpatterns = router.urls
