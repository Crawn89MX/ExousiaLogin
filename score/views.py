from score.serializers import ScoreSerializer
from rest_framework import viewsets
from score.models import Score

# Create your views here.

class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()