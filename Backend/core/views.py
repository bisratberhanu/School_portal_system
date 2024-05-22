from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet


class InitialUserViewSet(ModelViewSet):
    queryset = models.InitialUser.objects.all()
    serializer_class = serializers.InitialUserSerializer