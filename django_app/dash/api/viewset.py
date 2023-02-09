from django.contrib.auth.models import User
from rest_framework import viewsets
from api import serializers
from web.models import FamilyTree

# ViewSets define the view behavior.
class FamilyTreeViewSet(viewsets.ModelViewSet):
    queryset = FamilyTree.objects.all()
    serializer_class = serializers.FamilyTreeSerializer