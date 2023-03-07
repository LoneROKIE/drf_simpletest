from rest_framework import routers
from .api import ProjectViewSet

"""
Django rest framework crea las url con su propio metodo
"""

router = routers.DefaultRouter()

router.register('api/projects',ProjectViewSet, 'projects')

urlpatterns = router.urls
