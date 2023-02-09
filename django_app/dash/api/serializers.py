from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from web.models import FamilyTree

# Serializers define the API representation.
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyTree
        fields = ['id', 'name', 'gender']


class FamilyTreeSerializer(serializers.ModelSerializer):
    parent = ParentSerializer()
    class Meta:
        model = FamilyTree
        fields = ['id', 'name', 'gender', 'parent',]