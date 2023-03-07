from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # cualquier cliente puede solicitar datos a mi server
    serializer_class = ProjectSerializer