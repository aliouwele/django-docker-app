from rest_framework import routers
from api import views

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'opencellid', views.OpenCelliDViewSet)

urlpatterns = router.urls