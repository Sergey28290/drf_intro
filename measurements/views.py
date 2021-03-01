from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer, Measurement


class ProjectViewSet(ModelViewSet):
    """ViewSet для объекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Project.objects.all()
    serializer_class = MeasurementSerializer

# Create your views here.
