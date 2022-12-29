from rest_framework import routers
from .api import NoticeViewSet

router = routers.DefaultRouter()

router.register('api/noticias', NoticeViewSet, 'noticias')

urlpatterns = router.urls