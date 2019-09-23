from rest_framework.routers import SimpleRouter
from .views import OpViewset


router = SimpleRouter()
router.register(r'Operational', OpViewset)
urlpatterns = router.urls