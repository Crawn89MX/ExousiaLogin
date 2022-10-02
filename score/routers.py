from rest_framework import routers
from score.views import ScoreViewSet

router = routers.DefaultRouter()
router.register('score',ScoreViewSet,'score view set')

urlpatterns = router.urls