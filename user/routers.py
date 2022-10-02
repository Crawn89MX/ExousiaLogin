from rest_framework import routers
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register('user',UserViewSet,'User view set')

urlpatterns = router.urls